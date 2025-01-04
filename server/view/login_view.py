from typing import Dict

from fastapi import APIRouter, Body

from domain import login_domain
from helpers.authentication import Authentication
from schemas import AuthDetails, LoginToken, Password, Username

router = APIRouter(prefix="/api")
authentication = Authentication()


@router.post("/login")
def login(username: Username = Body(...), password: Password = Body(...)) -> LoginToken:
    auth_details = AuthDetails(username=username, password=password)

    return login_domain.login(auth_details=auth_details)
