from typing import List

from pydantic import BaseModel


class SerializedNode(BaseModel):
    node_properties: dict  # Should be a model that extends OSLModel
    node_type: str  # ENUM of the model labels


class RelationshipReactForceGraphInput(BaseModel):
    source: str
    target: str


class ReactForceGraphInput(BaseModel):
    nodes: List[SerializedNode]
    links: List[RelationshipReactForceGraphInput]
