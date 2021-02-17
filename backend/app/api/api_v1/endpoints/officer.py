from typing import List, Any

from fastapi import APIRouter, HTTPException

from api.api_v1.endpoints.util import get_nodes_and_relationships
from models.officer import OFFICER
from schema.officer import OfficerOut, OfficerIn, Officer
from schema.react_force_graph import ReactForceGraphInput

router = APIRouter()

model = OFFICER
label = model.__label__


@router.get("/", response_model=List[Officer])
def read_officers(skip: int = 0, limit: int = 25):
    results = model.nodes[skip:limit]
    return [Officer(**result.serialize.get("node_properties")) for result in results]


@router.get("/{node_id}", response_model=OfficerOut)
def read_officer(node_id: str) -> Any:
    node = model.nodes.get_or_none(node_id=node_id)
    if not node:
        raise HTTPException(status_code=404, detail=f"{label.title()} not found")
    return OfficerOut(**node.serialize.get("node_properties"), connected_nodes=node.serialize_connections)


@router.post("/search", response_model=List[OfficerOut])
def search_officers(query: OfficerIn, skip=0, limit=25) -> Any:
    filters = {k: v for k, v in query.dict().items() if v is not None}
    results = model.nodes.filter(**filters)
    return [OfficerOut(**result.serialize.get("node_properties"), connected_nodes=result.serialize_connections) for
            result in results]


@router.get("/{node_id}/react-force-graph", response_model=ReactForceGraphInput)
def custom_read_officer(node_id: str) -> Any:
    return get_nodes_and_relationships(model, node_id=node_id)
