from fastapi import APIRouter, Depends

from domain import logs_domain
from helpers.authentication import Authentication
from schemas import LogEntry, MongoPagination, Username

router = APIRouter(prefix="/api")
authentication = Authentication()


# This endpoint is intentionally left without logging to avoid excessive log entries
@router.get("/logs")
def get_logs(
    paginaton: MongoPagination = Depends(),
    _: Username = Depends(authentication.auth_wrapper),
) -> list[LogEntry] | None:
    logs = logs_domain.get_logs(paginaton=paginaton)

    return logs
