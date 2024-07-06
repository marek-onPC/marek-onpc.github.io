# marek_onpc.github.io


## Build image

`docker build -t server .`

## Run container

`docker run -dp 8000:8000 server`

## server's tests

`poetry run python -m pytest . -vv`
