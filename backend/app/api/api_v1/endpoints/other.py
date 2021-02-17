from typing import List, Any

from fastapi import APIRouter, HTTPException

from models.other import OTHER
from schema.other import OtherOut, Other, OtherIn

router = APIRouter()

model = OTHER
label = model.__label__


@router.get("/", response_model=List[Other])
def read_others(skip=0, limit=25):
    results = model.nodes[skip:limit]
    return [Other(**result.serialize.get("node_properties")) for result in results]


@router.get("/{node_id}", response_model=OtherOut)
def read_other(node_id: str) -> Any:
    node = model.nodes.get_or_none(node_id=node_id)
    if not node:
        raise HTTPException(status_code=404, detail=f"{label.title()} not found")
    return OtherOut(**node.serialize.get("node_properties"), connected_nodes=node.serialize_connections)


@router.post("/search", response_model=List[OtherOut])
def read_officers(query: OtherIn, skip=0, limit=25) -> Any:
    filters = {k: v for k, v in query.dict().items() if v is not None}
    results = model.nodes.filter(**filters)
    return [OtherOut(**result.serialize.get("node_properties"), connected_nodes=result.serialize_connections) for result in results]
