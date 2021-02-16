from fastapi import APIRouter
from starlette.responses import JSONResponse

from db.util import get_session

router = APIRouter()


@router.get("/")
def read_officers():
    query = """MATCH (n:OFFICER) RETURN n LIMIT 25"""

    with get_session() as session:
        tx = session.begin_transaction()
        result = tx.run(query)
        officers = [dict(i['n']) for i in result]
        tx.close()
    return JSONResponse(content={'officers': officers})


@router.get("/{id}")
def read_officer():
    pass