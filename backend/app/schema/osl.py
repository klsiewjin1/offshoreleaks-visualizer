from pydantic.main import BaseModel


class OSLModel(BaseModel):
    node_id: int
    name: str
    sourceID: str
    valid_until: str
    note: str
    country_codes: str
    countries: str
