from typing import Dict
from fastapi import APIRouter
from helpers.authentication import Authentication
from domain import login_domain
from schemas import AuthDetails, LoginToken, Password, Username
from fastapi import Body

router = APIRouter(prefix="/api")
authentication = Authentication()


@router.post("/login")
def login(username: Username = Body(...), password: Password = Body(...)) -> LoginToken:
    auth_details = AuthDetails(username=username, password=password)

    return login_domain.login(auth_details=auth_details)
