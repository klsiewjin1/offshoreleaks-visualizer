from fastapi import APIRouter

from api.api_v1.endpoints import officer

api_router = APIRouter()
api_router.include_router(officer.router, tags=["officer"])
