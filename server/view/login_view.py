from fastapi import APIRouter

from domain import login_domain
from helpers.authentication import Authentication
from schemas import AuthenticationDetails, LoginToken

router = APIRouter(prefix="/api")
authentication = Authentication()


@router.post("/login")
def login(auth_details: AuthenticationDetails) -> LoginToken:
    return login_domain.login(auth_details=auth_details)
