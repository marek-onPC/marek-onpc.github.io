FROM python:3.9.6

WORKDIR /server

COPY ./requirements.txt /server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt
RUN apt-get update && apt-get install libgl1 -y

COPY . .

# For local
# CMD ["uvicorn", "main:app"]

# For Heroku
CMD ["sh", "-c", "gunicorn -k uvicorn.workers.UvicornWorker main:app"]
