from fastapi import FastAPI

app = FastAPI()

@app.get("/noauth")
def noauthRoute():
    return "No need to auth"

@app.get("/withauth")
def withauthRoute():
    return "Auth required"