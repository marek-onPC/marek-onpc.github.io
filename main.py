from typing import Dict
from fastapi import Depends, FastAPI, HTTPException
from auth.authentication import Authentication
from auth.schemas import AuthDetails
from db.db_client import DatabaseClient
import bson.json_util as json_util

app = FastAPI()
authentication = Authentication()
db_client = DatabaseClient()

user = {
    "username": "name",
    "hashedPassword": "$2b$12$jwzb6rl2uspKNkJqNhv.z.kC36N.F3tQ5JzfywEgp422hufoHc7/C"
    # password is "password"
}

@app.post("/login")
def login(auth_details: AuthDetails):
    if auth_details.username != user["username"]:
        raise HTTPException(status_code=401, detail="Wrong user")

    if not authentication.verify_password(auth_details.password, user["hashedPassword"]):
        raise HTTPException(status_code=401, detail="Wrong password")
    
    token = authentication.encode_jwt(user["username"])

    return { "token" : token }


@app.get("/noauth")
def no_auth() -> str:
    return "No need to auth"


@app.get("/withauth")
def with_auth(username = Depends(authentication.auth_wrapper)) -> Dict:
    return { "name" : username }


@app.get("/login")
def no_auth() -> Dict:
    response = db_client.db_find_one("users", {"user" : "mareksmieja@gmail.com"})
    response_json = json_util._json_convert(response)

    return response_json
