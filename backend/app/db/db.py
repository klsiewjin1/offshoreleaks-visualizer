from neo4j import GraphDatabase

from core.config import settings

__auth = settings.NEO4J_AUTH.split("/")

driver = GraphDatabase.driver(
    "bolt://refinitiv-assignment_neo4j_1:7687",  # TODO fix this
    auth=(
        __auth[0], __auth[1]
    )
)