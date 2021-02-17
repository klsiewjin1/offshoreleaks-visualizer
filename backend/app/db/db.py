from neo4j import GraphDatabase
from neomodel import config

from core.config import settings

__auth = settings.NEO4J_AUTH.split("/")

driver = GraphDatabase.driver(
    f"bolt://{settings.PROJECT_NAME}_neo4j_1:7687",  # TODO fix this
    auth=(
        __auth[0], __auth[1]
    )
)
config.DATABASE_URL = f"bolt://{__auth[0]}:{__auth[1]}@{settings.PROJECT_NAME}_neo4j_1:7687"  # default
