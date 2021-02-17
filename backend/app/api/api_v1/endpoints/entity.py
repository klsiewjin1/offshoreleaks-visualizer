from typing import List, Any

from fastapi import APIRouter

from api.api_v1.endpoints.util import get_nodes_and_relationships, get_node_from_neomodel
from models.entity import ENTITY
from schema.entity import EntityOut, EntityIn, Entity
from schema.react_force_graph import ReactForceGraphInput

router = APIRouter()

model = ENTITY
label = model.__label__


@router.get("/", response_model=List[Entity])
def read_entities(skip: int = 0, limit: int = 25) -> Any:
    results = model.nodes[skip:limit]
    return [Entity(**result.serialize.get("node_properties")) for result in results]


@router.get("/{node_id}", response_model=EntityOut)
def read_entity(node_id: str, depth=1, skip=0, limit=25) -> Any:
    # TODO Implement a BFS to get nodes connected to the connected nodes
    node = get_node_from_neomodel(model, node_id=node_id)
    return EntityOut(**node.serialize.get("node_properties"), connected_nodes=node.serialize_connections)


@router.post("/search", response_model=List[EntityOut])
def search_entities(query: EntityIn, skip=0, limit=25) -> Any:
    filters = {k: v for k, v in query.dict().items() if v is not None}
    results = model.nodes.filter(**filters)
    return [EntityOut(**result.serialize.get("node_properties"), connected_nodes=result.serialize_connections) for
            result in results]


@router.get("/{node_id}/custom", response_model=ReactForceGraphInput)
def custom_read_entity(node_id: str) -> Any:
    return get_nodes_and_relationships(model, node_id=node_id)
