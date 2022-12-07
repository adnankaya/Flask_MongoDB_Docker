# Rest API development with Python, Flask, MongoDB, Docker

## Medium series
1. https://medium.com/@adnan-kaya/rest-api-development-with-python-flask-mongodb-docker-part-1-9129ad27983e
2. 


## Run MongoDB using docker
```bash

docker run --name mongodb -d -p 27017:27017 -e  MONGO_INITDB_ROOT_USERNAME=developer -e MONGO_INITDB_ROOT_PASSWORD=developer mongo
# 66663aab01ddff6f614ffd65a2b921b95aa0b26c175c58027e266fbbf2b2b746
docker ps -a
# CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                      NAMES
# 66663aab01dd   mongo     "docker-entrypoint.s…"   4 seconds ago   Up 3 seconds   0.0.0.0:27017->27017/tcp   mongodb
```
- MongoDB shell
```bash
docker exec -it mongodb mongosh -u developer -p developer
# show databases
test> show dbs

admin   100.00 KiB
config   12.00 KiB
local    72.00 KiB
```




