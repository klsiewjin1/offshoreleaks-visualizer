from typing import Optional

from pydantic.main import BaseModel


class OSLModel(BaseModel):
    node_id: str
    name: str
    sourceID: str
    valid_until: str
    note: str
    country_codes: str
    countries: str


class OSLModelIn(BaseModel):
    node_id: Optional[str]
    name: Optional[str]
    sourceID: Optional[str]
    valid_until: Optional[str]
    note: Optional[str]
    country_codes: Optional[str]
    countries: Optional[str]


class OSLModelOut(OSLModel):
    connected_nodes: Optional[list]
