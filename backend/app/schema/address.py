from typing import Optional, Any

from schema.osl import OSLModel, OSLModelIn


class BaseAddress(OSLModel):
    address: str


class AddressOut(BaseAddress):
    connected_nodes: Optional[list]


class Address(BaseAddress):
    pass


class AddressIn(OSLModelIn):
    address: Optional[str]
