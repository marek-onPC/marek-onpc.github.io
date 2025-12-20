# marek_onpc.github.io
## Description
This repository contains a codebase for my personal project, a web application for managing cheat sheets, code snippets, and other useful information. The application consists of a backend server built with Python + FastAPI and a frontend client developed using SvelteKit (SPA).

I'm always trying to modify and improve the codebase. If I can, I will add new features, fix bugs, or refactor existing code to make it cleaner and more efficient. It serves as a personal project to enhance my skills in web development and software engineering - a programming playground.

**Architecture overview:**
<details>
    <summary><strong>Login flow</strong></summary>
    <img src="architecture/login.svg" alt="architecture overview - login flow"/>
</details>
<details>
    <summary><strong>Cheat-sheet flow</strong></summary>
    <img src="architecture/cheat-sheet.svg" alt="architecture overview - cheat-sheet flow"/>
</details>

<br>

## Development plan, improvements

-  **<span style="color:green">DONE</span>** ~~Refactor server codebase, use typed models and schemas, implement linters and formatters (Python)~~
-  **<span style="color:green">DONE</span>** ~~Add cheat sheet/snipped full view modal (client application)~~
-  **<span style="color:green">DONE</span>** ~~Refactor server's databaseconenction class (singleton)~~
-  **<span style="color:green">DONE</span>** ~~Refactor authentication flow (to cover password and refresh token login)~~
-  **<span style="color:green">DONE</span>** ~~Adjust client to reauthenticate with refresh token~~
- **<span style="color:orange">DONE</span>** ~~Create a full architecture and data flow diagrams~~
- **<span style="color:blue">PLANNED</span>** Optimise REST API endpoints (reduce number of calls, batch requests)
- **<span style="color:blue">PLANNED</span>** Create `docker-compose` setup for local development (server, database)
- **<span style="color:green">DONE</span>** ~~Add hot-reloading for the server (during development)~~
- **<span style="color:green">DONE</span>** ~~Add test coverage reports (server)~~
- **<span style="color:yellow">IN PROGRESS</span>** Create a async logging/history system based on AMQP
- **<span style="color:blue">PLANNED</span>** Add Github Actions for CI/CD (test flows)
- **<span style="color:blue">PLANNED</span>** Fully test client codebase
- **<span style="color:blue">PLANNED</span>** Add a search engine for the cheat sheets (based on content)

<br>

## Docker setup

Instal docker via homebrew (this provides everything - the daemon, GUI dashboard, and Docker CLI integration):
```bash
brew install --cask docker
```

## Commands
### Server

Run those from the `./server` directory.

#### Run server
`APP_TYPE=fastapi poetry run uvicorn main:app --host 0.0.0.0 --port 8000`

#### Run server (in dev mode - reload on changes)
`APP_TYPE=fastapi poetry run fastapi dev main.py`

#### Run message broker worker (Celery)
`APP_TYPE=celery poetry run celery -A main worker --loglevel=info`

#### Run RabbitMQ (via Docker)
`docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4-management`

#### Run MongoDB (via Docker)
`docker run -d --name mongodb -p 27017:27017 mongo`

#### Tests
`APP_TYPE=fastapi poetry run python -m pytest . -vv`

#### Formatting, types, imports
`isort . && black . && flake8 . && mypy .`

---
### Dockerized server

#### Build image
`docker build -t server .`

#### Run container
`docker run -dp 8000:8000 server`

---
### Client

Run those from the `./client` directory.

#### Run dev server (SvelteKit)
`yarn dev`

#### Build client
`yarn build`

#### Tests
`yarn test`

#### Format, types, imports
`yarn format && yarn check && yarn lint`
