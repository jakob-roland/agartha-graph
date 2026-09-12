# Agartha — Jakob Rolands personal graph database

Purpose: Personal graph database to store everything, for example physical belongings, especially books, guidelines, like recipes, ideas, quotes, and reoccuring to-dos (health and maintenance schedules).  

Framework: JanusGraph <—— GremlinPython ——> Python Flask <—— JSON ——> Frontend (SvelteKit)

## JanusGraph with docker
JanusGraph Server is run via a Docker Container. The data is stored outside of the container, so it can be deleted and reconfigured safely. The path to the data folder is:  
`/home/jakob/Desktop/agartha-graph/backend/graph-data`

This command initiates the Docker Container:  
`$ docker run -d   --name agartha   -p 8182:8182   -v /home/jakob/Desktop/agartha-graph/backend/graph-data:/var/lib/janusgraph/data   janusgraph/janusgraph:latest`
