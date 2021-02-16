from typing import Optional, Any

from pydantic.schema import date

from schema.osl import OSLModel


class BaseEntity(OSLModel):
    jurisdiction: str
    jurisdiction_description: str
    incorporation_date: date
    inactivation_date: Optional[str]
    struck_off_date: date
    closed_date: date
    ibcRUC: Any
    status: Optional[str]
    company_type: str
