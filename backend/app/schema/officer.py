from typing import Optional

from pydantic import BaseModel

from schema.osl import OSLModel


class BaseOfficer(OSLModel):
    status: str


class OfficerIn(BaseModel):
    node_id: Optional[str]
    name: Optional[str]
    sourceID: Optional[str]
    valid_until: Optional[str]
    note: Optional[str]
    country_codes: Optional[str]
    countries: Optional[str]


class OfficerOut(BaseOfficer):
    pass


class OfficerInDB(BaseOfficer):
    id: int


class Officer(BaseOfficer):
    pass
