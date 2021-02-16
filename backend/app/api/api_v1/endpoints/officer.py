from typing import List, Any

from fastapi import APIRouter

from db.util import run_get_query
from schema.officer import OfficerOut, OfficerIn, Officer

router = APIRouter()


@router.get("/", response_model=List[OfficerOut])
def read_officers(skip=0, limit=25):
    query = f"""MATCH (n:OFFICER) RETURN n SKIP {skip} LIMIT {limit}"""
    officers = run_get_query(query)
    return [Officer(**officer) for officer in officers]


@router.get("/{node_id}", response_model=OfficerOut)
def read_officer(node_id: str) -> Any:
    query = f"""MATCH (n:OFFICER) WHERE n.node_id = "{node_id}" RETURN n"""
    officers = run_get_query(query)
    return Officer(**officers[0])


@router.post("/search", response_model=List[OfficerOut])
def search_officers(query: OfficerIn, skip=0, limit=25) -> Any:
    filters = []
    for filter_attr in query.dict():
        if query.__getattribute__(filter_attr):
            filters.append(f"""n.{filter_attr} = "{query.__getattribute__(filter_attr)}" """)

    query = f"""MATCH (n:OFFICER) WHERE ({" AND ".join(filters)}) RETURN n SKIP {skip} LIMIT {limit} """
    officers = run_get_query(query)
    return [Officer(**officer) for officer in officers]
