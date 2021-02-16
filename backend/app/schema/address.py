from typing import Optional


from schema.osl import OSLModel, OSLModelIn


class BaseAddress(OSLModel):
    address: str


class AddressOut(BaseAddress):
    pass


class Address(BaseAddress):
    pass


class AddressIn(OSLModelIn):
    address: Optional[str]
