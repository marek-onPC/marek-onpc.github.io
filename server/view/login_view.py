from typing import Dict
from fastapi import APIRouter
from server.auth.authentication import Authentication
from server.domain import login_domain
from server.schemas.schemas import AuthDetails
from fastapi import Body

router = APIRouter(prefix="/api")
authentication = Authentication()


@router.post("/login")
def login(username: str = Body(...), password: str = Body(...)) -> Dict:
    auth_details = AuthDetails(username=username, password=password)

    return login_domain.login(auth_details=auth_details)
