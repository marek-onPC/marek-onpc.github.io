# marek_onpc.github.io


## Dockerized server

### Build image

`docker build -t server .`

### Run container

`docker run -dp 8000:8000 server`


## Server

### Run server

`poetry run uvicorn main:app --host 0.0.0.0 --port 8000`

### Tests

`poetry run python -m pytest . -vv`
