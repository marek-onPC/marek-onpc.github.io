from typing import Dict
from adapter import user_adapter
from fastapi import HTTPException
from helpers.authentication import Authentication
from schemas import AuthDetails, LoginToken

authentication = Authentication()

def login(auth_details: AuthDetails) -> LoginToken:
    user = user_adapter.get_user(username=auth_details.username)

    if user is None:
        raise HTTPException(status_code=401, detail="Wrong user")

    if not authentication.verify_password(password=auth_details.password, hashed_password=user.password):
        raise HTTPException(status_code=401, detail="Wrong password")
    
    token = authentication.encode_jwt(user.username)

    return LoginToken(token=token)
