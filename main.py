import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.authentication import Authentication

from api import login, authpath, notes, note
from view import note_view

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]

origins = [
    "https://marek-onpc.github.io",
    "http://localhost:3000"
]

app = FastAPI()
authentication = Authentication()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(login.router)
app.include_router(authpath.router)
app.include_router(note_view.router)
