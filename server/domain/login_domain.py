from typing import Dict, Optional
from server.adapter import login_adapter
from fastapi import HTTPException
from server.auth.authentication import Authentication
from server.domain import authorization_domain
from server.schemas.schemas import AuthDetails

authentication = Authentication()

def login(auth_details: AuthDetails) -> Dict:
    user = login_adapter.login(username=auth_details.username)

    if user is None:
        raise HTTPException(status_code=401, detail="Wrong user")

    if not authentication.verify_password(auth_details.password, user.password):
        raise HTTPException(status_code=401, detail="Wrong password")
    
    token = authentication.encode_jwt(user.username)

    return { "token" : token }
