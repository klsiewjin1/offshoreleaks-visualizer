from typing import List, Any

from fastapi import APIRouter, HTTPException

from api.api_v1.endpoints.util import get_nodes_and_relationships
from models.intermediary import INTERMEDIARY
from schema.intermediary import IntermediaryOut, IntermediaryIn, Intermediary
from schema.react_force_graph import ReactForceGraphInput

router = APIRouter()

model = INTERMEDIARY
label = model.__label__


@router.get("/", response_model=List[Intermediary])
def read_intermediaries(skip:int=0, limit:int=25) -> Any:
    results = model.nodes[skip:limit]
    return [Intermediary(**result.serialize.get("node_properties")) for result in results]


@router.get("/{node_id}", response_model=IntermediaryOut)
def read_intermediary(node_id: str) -> Any:
    node = model.nodes.get_or_none(node_id=node_id)
    if not node:
        raise HTTPException(status_code=404, detail=f"{label.title()} not found")
    return IntermediaryOut(**node.serialize.get("node_properties"), connected_nodes=node.serialize_connections)


@router.post("/search", response_model=List[IntermediaryOut])
def search_intermediaries(query: IntermediaryIn, skip=0, limit=25) -> Any:
    filters = {k: v for k, v in query.dict().items() if v is not None}
    results = model.nodes.filter(**filters)
    return [IntermediaryOut(**result.serialize.get("node_properties"), connected_nodes=result.serialize_connections) for result in results]

@router.get("/{node_id}/react-force-graph", response_model=ReactForceGraphInput)
def custom_read_intermediary(node_id: str) -> Any:
    return get_nodes_and_relationships(model, node_id=node_id)