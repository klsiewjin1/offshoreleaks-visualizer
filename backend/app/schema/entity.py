from typing import Optional, Any

from pydantic.schema import date

from schema.osl import OSLModel, OSLModelIn


class BaseEntity(OSLModel):
    jurisdiction: str
    jurisdiction_description: str
    incorporation_date: str
    inactivation_date: Optional[str]
    struck_off_date: str
    closed_date: str
    ibcRUC: str
    status: Optional[str]
    company_type: str


class EntityOut(BaseEntity):
    connected_nodes: Optional[list]


class Entity(BaseEntity):
    pass


class EntityIn(OSLModelIn):
    jurisdiction: Optional[str]
    jurisdiction_description: Optional[str]
    incorporation_date: Optional[date]
    inactivation_date: Optional[str]
    struck_off_date: Optional[date]
    closed_date: Optional[date]
    ibcRUC: Optional[str]
    status: Optional[str]
    company_type: Optional[str]