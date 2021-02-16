from pydantic import BaseModel


class BaseOfficer(BaseModel):
    sourceID: str
    note: str
    valid_until: str
    name: str
    country_codes: str
    countries: str
    node_id: str
    status: str


class OfficerIn(BaseOfficer):
    pass
