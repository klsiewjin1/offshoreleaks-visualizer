from typing import Optional, Any

from schema.osl import OSLModel, OSLModelIn


class BaseIntermediary(OSLModel):
    pass


class IntermediaryOut(BaseIntermediary):
    connected_nodes: Optional[list]

class Intermediary(BaseIntermediary):
    pass


class IntermediaryIn(OSLModelIn):
    pass
