cd /var/lib/neo4j/import/ || exit
../bin/neo4j-admin import --database="$OSL_NEO4J_DB_NAME" --nodes=ADDRESS=paradise_papers.nodes.address.csv --nodes=OFFICER=paradise_papers.nodes.officer.csv --nodes=ENTITY=paradise_papers.nodes.entity.csv --nodes=INTERMEDIARY=paradise_papers.nodes.intermediary.csv --nodes=OTHER=paradise_papers.nodes.other.csv --relationships=paradise_papers.edges.csv --skip-bad-relationships
chown -R neo4j /var/lib/neo4j/data/databases/"$OSL_NEO4J_DB_NAME"
#echo "dbms.default_database=oslviz" > conf