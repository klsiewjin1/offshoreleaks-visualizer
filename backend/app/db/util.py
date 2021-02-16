from db.db import driver
from schema.osl import OSLModelIn


def get_session():
    return driver.session()


def generate_filter(query_in: OSLModelIn):
    filters = []
    for filter_attr in query_in.dict():
        if query_in.__getattribute__(filter_attr):
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
