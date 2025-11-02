from fastapi import APIRouter, Response

from domain import login_domain
from helpers.authentication import Authentication
from helpers.events import EventTypes, send_log_event
from schemas import AllowedGrandTypes, AuthenticationDetails, AuthToken

router = APIRouter(prefix="/api")
authentication = Authentication()


@router.post("/login", response_model=AuthToken)
def login(auth_details: AuthenticationDetails) -> Response:
    log_message = (
        "Login attempt via password"
        if auth_details.grant_type == AllowedGrandTypes.PASSWORD
        else "Login attempt via refresh_token"
    )

    send_log_event(
        event_type=EventTypes.LOGIN_ATTEMPT,
        message=log_message,
        user=(
            auth_details.username
            if auth_details.grant_type == AllowedGrandTypes.PASSWORD
            else None
        ),
        context={"status": "started", "grant_type": auth_details.grant_type},
    )

    try:
        token = login_domain.get_token(auth_details=auth_details).model_dump_json()
    except Exception as e:
        send_log_event(
            event_type=EventTypes.LOGIN_ATTEMPT,
            message=log_message,
            user=(
                auth_details.username
                if auth_details.grant_type == AllowedGrandTypes.PASSWORD
                else None
            ),
            context={
                "status": "failed",
                "grant_type": auth_details.grant_type,
                "error": str(e),
            },
        )
        raise e

    response = Response(
        content=token,
        media_type="application/json",
        status_code=200,
        headers={"cache-control": "no-store"},
    )

    send_log_event(
        event_type=EventTypes.LOGIN_ATTEMPT,
        message=log_message,
        user=(
            auth_details.username
            if auth_details.grant_type == AllowedGrandTypes.PASSWORD
            else None
        ),
        context={"status": "successful", "grant_type": auth_details.grant_type},
    )

    return response
