from typing import Any, Optional

from schema.osl import OSLModel, OSLModelIn


class BaseOfficer(OSLModel):
    status: str


class OfficerIn(OSLModelIn):
    pass


class OfficerOut(BaseOfficer):
    connected_nodes: Optional[list]


class OfficerInDB(BaseOfficer):
    id: int


class Officer(BaseOfficer):
    pass
