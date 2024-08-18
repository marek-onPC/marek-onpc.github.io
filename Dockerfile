FROM python:3.11.0

WORKDIR /server

COPY ./server/pyproject.toml /server/pyproject.toml
COPY ./server/poetry.lock /server/poetry.lock

RUN pip install poetry
RUN apt-get update && apt-get install libgl1 -y

RUN poetry install

COPY ./server .

# For local
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${PORT:-8000}"]

# For Heroku
# CMD ["sh", "-c", "gunicorn -k uvicorn.workers.UvicornWorker main:app"]
