from typing import List, Any

from fastapi import APIRouter, HTTPException

from models.address import ADDRESS
from schema.address import AddressOut, Address, AddressIn

router = APIRouter()

model = ADDRESS
label = model.__label__


@router.get("/", response_model=List[Address])
def read_addresses(skip: int = 0, limit: int = 25) -> Any:
    results = model.nodes[skip:limit]
    return [Address(**result.serialize.get("node_properties")) for result in results]


@router.get("/{node_id}", response_model=AddressOut)
def read_address(node_id: str) -> Any:
    node = model.nodes.get_or_none(node_id=node_id)
    if not node:
        raise HTTPException(status_code=404, detail=f"{label.title()} not found")
    return AddressOut(**node.serialize.get("node_properties"), connected_nodes=node.serialize_connections)


@router.post("/search", response_model=List[AddressOut])
def search_addresses(query: AddressIn, skip=0, limit=25) -> Any:
    filters = {k: v for k, v in query.dict().items() if v is not None}
    results = model.nodes.filter(**filters)
    return [AddressOut(**result.serialize.get("node_properties"), connected_nodes=result.serialize_connections) for
            result in results]
