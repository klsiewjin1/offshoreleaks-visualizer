from typing import List, Any

from fastapi import APIRouter, HTTPException

from db.util import run_get_query, generate_filter
from schema.address import AddressOut, Address, AddressIn

router = APIRouter()

label = "ADDRESS"


@router.get("/", response_model=List[AddressOut])
def read_addresses(skip=0, limit=25) -> Any:
    query = f"""MATCH (n:{label}) RETURN n SKIP {skip} LIMIT {limit}"""
    results = run_get_query(query)
    return [Address(**result) for result in results]


@router.get("/{node_id}", response_model=AddressOut)
def read_address(node_id: str) -> Any:
    query = f"""MATCH (n:{label}) WHERE n.node_id = "{node_id}" RETURN n LIMIT 1"""
    results = run_get_query(query)
    if len(results) == 0:
        raise HTTPException(status_code=404, detail=f"{label.title()} not found")
    return Address(**results[0])


@router.post("/search", response_model=List[AddressOut])
def search_addresses(query: AddressIn, skip=0, limit=25) -> Any:
    query_filter = generate_filter(query)
    query = f"""MATCH (n:{label}) WHERE ({query_filter}) RETURN n SKIP {skip} LIMIT {limit} """
    results = run_get_query(query)
    return [Address(**result) for result in results]
