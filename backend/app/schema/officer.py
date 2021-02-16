from schema.osl import OSLModel


class BaseOfficer(OSLModel):
    status: str


class OfficerIn(BaseOfficer):
    pass


class OfficerOut(BaseOfficer):
    pass


class OfficerInDB(BaseOfficer):
    id: int