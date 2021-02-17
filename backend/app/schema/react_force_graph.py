from typing import List, Optional

from pydantic import BaseModel


# class SerializedNode(BaseModel):
#     node_properties: dict  # Should be a model that extends OSLModel
#     node_type: str  # ENUM of the model labels


class RelationshipReactForceGraphInput(BaseModel):
    source: str
    target: str
    name: Optional[str]


class GraphNode(BaseModel):
    name: str
    node_id: str
    node_type: str


class ReactForceGraphInput(BaseModel):
    nodes: List[GraphNode]
    links: List[RelationshipReactForceGraphInput]
