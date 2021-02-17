from typing import List, Optional

from pydantic import BaseModel


# class SerializedNode(BaseModel):
#     node_properties: dict  # Should be a model that extends OSLModel
#     node_type: str  # ENUM of the model labels


class RelationshipReactForceGraphInput(BaseModel):
    source: str
    target: str
    name: Optional[str]


class ReactForceGraphInput(BaseModel):
    nodes: List[dict]
    links: List[RelationshipReactForceGraphInput]
