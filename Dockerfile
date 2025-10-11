FROM python:3.11.0

WORKDIR /server

COPY ./server/pyproject.toml /server/pyproject.toml

RUN pip install poetry==1.8.3
RUN apt-get update && apt-get install libgl1 -y

RUN poetry export --without-hashes --format requirements.txt --output /server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

COPY ./server .

# For local
# CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# For Heroku
# CMD ["sh", "-c", "gunicorn -k uvicorn.workers.UvicornWorker main:app"]

ARG SERVERTYPE

# Use shell logic to determine which server to install
CMD if [ "$SERVERTYPE" = "fastapi" ]; then \
      echo "Starting FastAPI server..." && \
      gunicorn -k uvicorn.workers.UvicornWorker main:app; \
    elif [ "$SERVERTYPE" = "celery" ]; then \
      echo "Starting Celery worker..." && \
      poetry run celery -A main worker --loglevel=info; \
    else \
      echo "Unknown SERVERTYPE: $SERVERTYPE" && exit 1; \
    fi
