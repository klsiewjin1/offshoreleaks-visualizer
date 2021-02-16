from typing import Optional, Any

from pydantic.schema import date

from schema.osl import OSLModel, OSLModelIn


class BaseEntity(OSLModel):
    jurisdiction: str
    jurisdiction_description: str
    incorporation_date: date
    inactivation_date: Optional[str]
    struck_off_date: date
    closed_date: date
    ibcRUC: str
    status: Optional[str]
    company_type: str


class EntityOut(BaseEntity):
    pass


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