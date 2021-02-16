from fastapi import FastAPI

from api.api_v1.api import api_router
from core.config import settings
from db.db import driver
from db.util import get_session

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.on_event("startup")
def init_db():
    db = driver
    session = db.session()
    try:
        session.run("Match () Return 1 Limit 1")
        print("Connected to Neo4J database")
    except Exception:
        print("Failed to connect to Neo4J database")


@app.on_event("shutdown")
def close_db_connection():
    session = get_session()
    session.close()


app.include_router(api_router, prefix=settings.API_V1_STR)
