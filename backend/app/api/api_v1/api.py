from fastapi import APIRouter

from api.api_v1.endpoints import officer, address, entity, intermediary, other

api_router = APIRouter()
api_router.include_router(address.router, prefix="/addresses", tags=["address"])
api_router.include_router(entity.router, prefix="/entities", tags=["entity"])
api_router.include_router(intermediary.router, prefix="/intermediaries", tags=["intermediary"])
api_router.include_router(officer.router, prefix="/officers", tags=["officer"])
api_router.include_router(other.router, prefix="/others", tags=["other"])
