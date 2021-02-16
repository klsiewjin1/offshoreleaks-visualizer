from fastapi import APIRouter

from api.api_v1.endpoints import officer, address

api_router = APIRouter()
api_router.include_router(officer.router, prefix="/officers", tags=["officer"])
api_router.include_router(address.router, prefix="/addresses", tags=["address"])
