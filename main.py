from fastapi import FastAPI
from auth.authentication import Authentication
from auth.schemas import AuthDetails

app = FastAPI()

@app.get("/noauth")
def noauthRoute():
    return "No need to auth"

@app.get("/withauth")
def withauthRoute():
    return "Auth required"