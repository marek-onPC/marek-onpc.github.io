from typing import Dict, Optional
from adapter import login_adapter
from fastapi import HTTPException
from auth.authentication import Authentication
from domain import authorization_domain
from schemas.schemas import AuthDetails

authentication = Authentication()

def login(auth_details: AuthDetails, photo: Optional[str]) -> Dict:
    user = login_adapter.login(username=auth_details.username)

    if user is None:
        raise HTTPException(status_code=401, detail="Wrong user")

    if not authentication.verify_password(auth_details.password, user.password):
        raise HTTPException(status_code=401, detail="Wrong password")
    
    if photo and not authorization_domain.verify_photo(user=user, photo=photo):
        raise HTTPException(status_code=401, detail="Not authorized")
    
    token = authentication.encode_jwt(user.username)

    return { "token" : token }
