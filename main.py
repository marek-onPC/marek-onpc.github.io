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
def login(authDetailes: AuthDetails):
    if authDetailes.username != user["username"]:
        raise HTTPException(status_code=401, detail="Wrong user")

    if not authentication.verifyPassword(authDetailes.password, user["hashedPassword"]):
        raise HTTPException(status_code=401, detail="Wrong password")
    
    token = authentication.encodeJWT(user["username"])

    return { "token" : token }

@app.get("/noauth")
def noauthRoute():
    return "No need to auth"

@app.get("/withauth")
def withauthRoute(username = Depends(authentication.authWrapper)):
    return { "name" : username }