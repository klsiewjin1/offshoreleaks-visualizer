from typing import List, Any

from fastapi import APIRouter, HTTPException

from db.util import run_get_query, generate_filter
from schema.other import OtherOut, Other, OtherIn

router = APIRouter()

label = "OTHER"


@router.get("/", response_model=List[OtherOut])
def read_officers(skip=0, limit=25):
    query = f"""MATCH (n:{label}) RETURN n SKIP {skip} LIMIT {limit}"""
    results = run_get_query(query)
    return [Other(**result) for result in results]


@router.get("/{node_id}", response_model=OtherOut)
def read_officer(node_id: str) -> Any:
    query = f"""MATCH (n:{label}) WHERE n.node_id = "{node_id}" RETURN n LIMIT 1"""
    results = run_get_query(query)
    if len(results) == 0:
        raise HTTPException(status_code=404, detail=f"{label.title()} not found")
    return Other(**results[0])


@router.post("/search", response_model=List[OtherOut])
def search_officers(query: OtherIn, skip=0, limit=25) -> Any:
    query_filter = generate_filter(query)
    query = f"""MATCH (n:{label}) WHERE ({query_filter}) RETURN n SKIP {skip} LIMIT {limit} """
    results = run_get_query(query)
    return [Other(**result) for result in results]
