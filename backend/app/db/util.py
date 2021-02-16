from db.db import driver


def get_session():
    return driver.session()


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
