FROM python:3.11.0

ENV PORT $PORT

WORKDIR /server

RUN pip install poetry
RUN apt-get update && apt-get install libgl1 -y

RUN poetry export --without-hashes --format requirements.txt --output /server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

COPY ./server .

# For local
# CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${PORT:-8000}"]

# For Heroku
CMD ["sh", "-c", "gunicorn -k uvicorn.workers.UvicornWorker main:app"]
