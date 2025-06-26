from fastapi import APIRouter, Response

from domain import login_domain
from helpers.authentication import Authentication
from schemas import AuthenticationDetails, AuthToken

router = APIRouter(prefix="/api")
authentication = Authentication()


@router.post("/login", response_model=AuthToken)
def login(auth_details: AuthenticationDetails) -> Response:
    token = login_domain.get_token(auth_details=auth_details).model_dump_json()

    response = Response(
        content=token,
        media_type="application/json",
        status_code=200,
        headers={"cache-control": "no-store"},
    )

    return response
