import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from helpers.events import celery
from view import cheat_sheet_view, login_view

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
amqp_url = os.environ["AMQP_URL"]

origins = ["https://marek-onpc.github.io", "http://localhost:3000"]

if os.environ.get("APP_TYPE") == "celery":
    celery

if os.environ.get("APP_TYPE") == "fastapi":
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(login_view.router)
    app.include_router(cheat_sheet_view.router)
