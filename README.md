# Rest API development with Python, Flask, MongoDB, Docker

## Medium series
1. https://medium.com/@adnan-kaya/rest-api-development-with-python-flask-mongodb-docker-part-1-9129ad27983e
2. https://medium.com/@adnan-kaya/rest-api-development-with-python-flask-mongodb-docker-part-2-74324e12d90f
3. https://medium.com/@adnan-kaya/rest-api-development-with-python-flask-mongodb-docker-part-3-ce8c58f72620
4. 


## Run Tests
```
docker compose exec web sh -c "pytest -s --disable-warnings"
```
## Run MongoDB using docker
```bash

docker compose up -d --build
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




