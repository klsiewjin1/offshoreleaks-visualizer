from typing import Optional

from schema.osl import OSLModel, OSLModelIn


class BaseOther(OSLModel):
    pass


class OtherOut(BaseOther):
    connected_nodes: Optional[list]


class Other(BaseOther):
    pass


class OtherIn(OSLModelIn):
    pass
