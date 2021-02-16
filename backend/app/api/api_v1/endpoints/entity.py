from typing import List, Any

from fastapi import APIRouter, HTTPException

from db.util import run_get_query, generate_filter
from schema.entity import EntityOut, Entity, EntityIn

router = APIRouter()

label = "ENTITY"


@router.get("/", response_model=List[EntityOut])
def read_entities(skip=0, limit=25) -> Any:
    query = f"""MATCH (n:{label}) RETURN n SKIP {skip} LIMIT {limit}"""
    results = run_get_query(query)
    return [Entity(**result) for result in results]


@router.get("/{node_id}", response_model=EntityOut)
def read_entity(node_id: str) -> Any:
    query = f"""MATCH (n:{label}) WHERE n.node_id = "{node_id}" RETURN n LIMIT 1"""
    results = run_get_query(query)
    if len(results) == 0:
        raise HTTPException(status_code=404, detail=f"{label.title()} not found")
    return Entity(**results[0])


@router.post("/search", response_model=List[EntityOut])
def search_entities(query: EntityIn, skip=0, limit=25) -> Any:
    query_filter = generate_filter(query)
    query = f"""MATCH (n:{label}) WHERE ({query_filter}) RETURN n SKIP {skip} LIMIT {limit} """
    results = run_get_query(query)
    return [Entity(**result) for result in results]

