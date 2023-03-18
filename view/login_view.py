from typing import Dict
from fastapi import APIRouter
from auth.authentication import Authentication
from domain import login_domain
from schemas.schemas import AuthDetails

router = APIRouter(prefix="/api")
authentication = Authentication()


@router.post("/login")
def login(auth_details: AuthDetails) -> Dict:
    return login_domain.login(auth_details=auth_details)
