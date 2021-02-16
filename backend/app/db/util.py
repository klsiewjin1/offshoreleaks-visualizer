from neo4j import Session

from db.db import driver
from schema.osl import OSLModelIn


def get_session() -> Session:
    return driver.session()


def generate_filter(query_in: OSLModelIn) -> str:
    filters = []
    for filter_attr in query_in.dict():
        attr = query_in.__getattribute__(filter_attr)
        if attr and isinstance(attr, str):
            filters.append(f"""n.{filter_attr} = "{query_in.__getattribute__(filter_attr)}" """)

    return " AND ".join(filters)


def run_get_query(query):
    with get_session() as session:
        tx = session.begin_transaction()
        result = tx.run(query)
        holder = [dict(i['n']) for i in result]
        tx.close()
        return holder


def run_post_query(query, data):
    def put(tx, query, data):
        return tx.run(query, **data).single().value()

    session = get_session()
    result = session.write_transaction(put, query, data)
    session.close()
    return result
