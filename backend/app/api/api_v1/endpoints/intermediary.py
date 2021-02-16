from typing import List, Any

from fastapi import APIRouter, HTTPException

from db.util import run_get_query, generate_filter
from schema.intermediary import IntermediaryOut, IntermediaryIn, Intermediary

router = APIRouter()

label = "INTERMEDIARY"


@router.get("/", response_model=List[IntermediaryOut])
def read_intermediaries(skip=0, limit=25) -> Any:
    query = f"""MATCH (n:{label}) RETURN n SKIP {skip} LIMIT {limit}"""
    result = run_get_query(query)
    return [Intermediary(**result) for result in result]


@router.get("/{node_id}", response_model=IntermediaryOut)
def read_intermediary(node_id: str) -> Any:
    query = f"""MATCH (n:{label}) WHERE n.node_id = "{node_id}" RETURN n LIMIT 1"""
    results = run_get_query(query)
    if len(results) == 0:
        raise HTTPException(status_code=404, detail=f"{label.title()} not found")
    return Intermediary(**results[0])


@router.post("/search", response_model=List[IntermediaryOut])
def search_intermediaries(query: IntermediaryIn, skip=0, limit=25) -> Any:
    query_filter = generate_filter(query)
    query = f"""MATCH (n:{label}) WHERE ({query_filter}) RETURN n SKIP {skip} LIMIT {limit} """
    results = run_get_query(query)
    return [Intermediary(**result) for result in results]

