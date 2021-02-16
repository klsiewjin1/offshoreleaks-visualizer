from fastapi import FastAPI

from api.api_v1.api import api_router
from core.config import settings
from db.db import driver

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.on_event("startup")
def init_db():
    db = driver
    session = db.session()
    try:
        session.run("Match () Return 1 Limit 1")
        # tmp = session.run("MATCH (n:OTHER) RETURN n LIMIT 25")
        print('ok')
    except Exception:
        print('not ok')


app.include_router(api_router, prefix=settings.API_V1_STR)

