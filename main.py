from fastapi import Depends, FastAPI, HTTPException
from auth.authentication import Authentication
from auth.schemas import AuthDetails

app = FastAPI()
authentication = Authentication()

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
def no_auth():
    return "No need to auth"

@app.get("/withauth")
def with_auth(username = Depends(authentication.auth_wrapper)):
    return { "name" : username }