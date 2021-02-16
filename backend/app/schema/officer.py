from schema.osl import OSLModel, OSLModelIn


class BaseOfficer(OSLModel):
    status: str


class OfficerIn(OSLModelIn):
    pass


class OfficerOut(BaseOfficer):
    pass


class OfficerInDB(BaseOfficer):
    id: int


class Officer(BaseOfficer):
    pass
