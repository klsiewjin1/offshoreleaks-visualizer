Setting the project up locally

###### Requirements
1. Docker
2. Git

`git pull` and `docker-compose up --build -d` should do the trick

This project sets up 3 components:
1. Neo4J database, with data from csv files. 
   - The `db/neo4j/import` folder will be mounted onto the `$neo4j_home/import` which is at /var/lib/neo4j/import. This is crucial as the `neo4j-admin` import tool uses files from the `import` folder
   - The `db/neo4j/conf` folder will be mouted onto the `$neo4j_home/conf`. Add `dbms.default_database=$OSL_NEO4J_DB_NAME` into the `$neo4j_home/conf/neo4j.conf` file. Since the Neo4J database we are running is the community edition, only 1 database can be used. 
   - Import the csv files into the database with `db/neo4j/import/init-neo4j.sh`. It will output something like this
   
```
root@fe5e8a69bdb5:/var/lib/neo4j/import# ../bin/neo4j-admin import --database=oslviz --nodes
=ADDRESS=paradise_papers.nodes.address.csv --nodes=OFFICER=paradise_papers.nodes.officer.csv
 --nodes=ENTITY=paradise_papers.nodes.entity.csv --nodes=INTERMEDIARY=paradise_papers.nodes.
intermediary.csv --nodes=OTHER=paradise_papers.nodes.other.csv --relationships=paradise_pape
rs.edges.csv --skip-bad-relationships

Neo4j version: 4.2.3
Importing the contents of these files into /data/databases/oslviz:
Nodes:
  [OTHER]:
  /var/lib/neo4j/import/paradise_papers.nodes.other.csv

  [ENTITY]:
  /var/lib/neo4j/import/paradise_papers.nodes.entity.csv

  [ADDRESS]:
  /var/lib/neo4j/import/paradise_papers.nodes.address.csv

  [OFFICER]:
  /var/lib/neo4j/import/paradise_papers.nodes.officer.csv

  [INTERMEDIARY]:
  /var/lib/neo4j/import/paradise_papers.nodes.intermediary.csv

Relationships:
  /var/lib/neo4j/import/paradise_papers.edges.csv


Available resources:
  Total machine memory: 12.43GiB
  Free machine memory: 8.102GiB
  Max heap memory : 2.764GiB
  Processors: 12
  Configured max memory: 8.701GiB
  High-IO: true


Import starting 2021-02-15 14:52:24.835+0000
  Estimated number of nodes: 965.66 k
  Estimated number of node properties: 10.54 M
  Estimated number of relationships: 1.65 M
  Estimated number of relationship properties: 8.23 M
  Estimated disk space usage: 644.1MiB
  Estimated required memory usage: 1.008GiB

(1/4) Node import 2021-02-15 14:52:24.857+0000
  Estimated number of nodes: 965.66 k
  Estimated disk space usage: 341.5MiB
  Estimated required memory usage: 1.008GiB
.......... .......... .......... .......... ..........   5% ∆1m 33s 773ms
.......... .......... .......... .......... ..........  10% ∆3ms
.......... .......... .......... .......... ..........  15% ∆3m 58s 585ms
.......... .......... .......... .......... ..........  20% ∆2ms
.......... .......... .......... .......... ..........  25% ∆1m 14s 667ms
.......... ..-....... .......... .......... ..........  30% ∆127ms
.......... .......... .......... .......... ..........  35% ∆1ms
.......... .......... .......... .......... ..........  40% ∆201ms
.......... .......... .......... .......... ..........  45% ∆208ms
.......... .......... .......... .......... ..........  50% ∆2ms
.......... .......... .......... .......... ..........  55% ∆1ms
.......... .......... .......... .......... ..........  60% ∆400ms
.......... .......... .......... .......... ..........  65% ∆2ms
.......... .......... .......... .......... ..........  70% ∆2ms
.......... .......... .......... .......... ..........  75% ∆19ms
.......... .......... .......... .......... ..........  80% ∆1ms
.......... .......... .......... .......... ..........  85% ∆3ms
.......... .......... .......... .......... ..........  90% ∆1ms
.......... .......... .......... .......... ..........  95% ∆0ms
.......... .......... .......... .......... .......... 100% ∆1ms

(2/4) Relationship import 2021-02-15 15:00:26.189+0000
  Estimated number of relationships: 1.65 M
  Estimated disk space usage: 302.6MiB
  Estimated required memory usage: 1.007GiB
.......... .......... .......... .......... ..........   5% ∆2m 32s 490ms
.......... .......... .......... .......... ..........  10% ∆1ms
.......... .......... .......... .......... ..........  15% ∆1ms
.......... .......... .......... .......... ..........  20% ∆0ms
.......... .......... .......... .......... ..........  25% ∆2m 49s 929ms
.......... .......... .......... .......... ..........  30% ∆1ms
.......... .......... .......... .......... ..........  35% ∆1ms
.......... .......... .......... .......... ..........  40% ∆1ms
.......... .......... .......... .......... ..........  45% ∆9s 208ms
.......... .......... .......... .......... ..........  50% ∆1ms
.......... .......... .......... .......... ..........  55% ∆2m 2s 295ms
.......... .......... .......... .......... ..........  60% ∆1ms
.......... .......... .......... .......... ..........  65% ∆3m 45s 770ms
.......... .......... .......... .......... ..........  70% ∆1ms
.......... .......... .......... .......... ..........  75% ∆1ms
.......... .......... .......... .......... ..........  80% ∆601ms
.......... .......... .......... .......... ..........  85% ∆7m 12s 899ms
.......... .......... .......... .......... ..........  90% ∆1ms
.......... .......... .......... .......... ..........  95% ∆1ms
.......... .......... .......... .......... .......... 100% ∆1ms

(3/4) Relationship linking 2021-02-15 15:18:59.393+0000
  Estimated required memory usage: 1.005GiB
.......... .......... .......... .......... ..........   5% ∆202ms
.......... .......... .......... .......... ..........  10% ∆1ms
.......... .......... .......... .......... ..........  15% ∆1ms
.......... .......... .......... .......... -.........  20% ∆144ms
.......... .......... .......... .......... ..........  25% ∆1ms
.......... .......... .......... .......... ..........  30% ∆1ms
.......... .......... .......... .......... ..........  35% ∆0ms
.......... .......... .......... .......... ..........  40% ∆1ms
.......... .......... .......... ........-. ..........  45% ∆108ms
.......... .......... .......... .......... ..........  50% ∆201ms
.......... .......... .......... .......... ..........  55% ∆0ms
.......... .......... .......... .......... ..........  60% ∆1ms
.......... .......... .......... .......... ..........  65% ∆0ms
.......... .......... .......... .......... ..........  70% ∆2ms
.......... .......... .......... .......... ..........  75% ∆0ms
.......... .......... .......... .......... ..........  80% ∆1ms
.......... .......... .......... .......... ..........  85% ∆89ms
.......... .......... .......... .......... ..........  90% ∆0ms
.......... .......... .......... .......... ..........  95% ∆2ms
.......... .......... .......... .......... .......... 100% ∆0ms

(4/4) Post processing 2021-02-15 15:19:00.497+0000
  Estimated required memory usage: 1020MiB
-.-....... .......... .......... .......... ..........   5% ∆114ms
.......... .......... .......... .......... ..........  10% ∆1ms
.......... .......... .......... ......-... ..........  15% ∆54ms
.......... .......... .......... .......... ..........  20% ∆202ms
.......... .......... .......... .......... ..........  25% ∆0ms
.......... .......... .......... .......... ..........  30% ∆1ms
.......... .......... .......... .......... ..........  35% ∆1ms
.......... .......... .......... .......... ..........  40% ∆2ms
.......... .......... .......... .......... ..........  45% ∆1ms
.......... .......... .......... .......... ..........  50% ∆1ms
.......... .......... .......... .......... ..........  55% ∆1ms
.......... .......... .......... .......... ..........  60% ∆1ms
.......... .......... .......... .......... ..........  65% ∆2ms
.......... .......... .......... .......... ..........  70% ∆0ms
.......... .......... .......... .......... ..........  75% ∆1ms
.......... .......... .......... .......... ..........  80% ∆10s 177ms
.......... .......... .......... .......... ..........  85% ∆0ms
.......... .......... .......... .......... ..........  90% ∆1ms
.......... .......... .......... .......... ..........  95% ∆1ms
.......... .......... .......... .......... .......... 100% ∆1ms


IMPORT DONE in 26m 47s 878ms.
Imported:
  867931 nodes
  1657838 relationships
  17838925 properties
Peak memory usage: 1.040GiB

```
   
2. FastApi backend (WIP)
  - Easy to develop backend framework with strong validations and automatic schema generation.

3. React frontend (WIP)
 - Uses the react-force-graph library to convert nodes and relationships into graphs.
 - An alternative could be to utilize the neo4j-driver library directly to the neo4j database running. 

Done list
0. Setup docker-compose to ensure ease of development (with auto reloading) and deployment
1. Load Neo4J dataset into DB
2. Backend to pull data from Neo4J data
3. Simple frontend, using react-force-graph to display nodes from backend. Will always display Entity nodes first


TODO list
1. View the properties of a node
2. Clicking on a node will bring spawn connected nodes, which will then be added and displayed
    - bugs to fix: hashmap for nodes and links 
3. More views/visualizations
4. Graph traversals between different nodes will visually create a path from 1 node to another
5. Most popular node in a graph "by most relationships"