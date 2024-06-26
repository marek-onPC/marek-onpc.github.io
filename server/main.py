import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.view import note_view, login_view

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]

origins = [
    "https://marek-onpc.github.io",
    "http://localhost:3000"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(login_view.router)
app.include_router(note_view.router)
