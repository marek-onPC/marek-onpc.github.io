from typing import Literal, Optional

from fastapi import APIRouter, Depends

from domain import cheat_sheet_domain
from helpers.authentication import Authentication
from helpers.events import send_log_event
from helpers.serializers import bool_list_serializer
from schemas import (
    CheatSheetID,
    CheatSheetSchema,
    EventTypes,
    MongoDelete,
    MongoInsert,
    MongoUpdate,
    UnsavedCheatSheetSchema,
    UpdateCheatSheetSchema,
    Username,
)

router = APIRouter(prefix="/api")
authentication = Authentication()


@router.get("/cheat_sheets")
def get_cheat_sheets(
    is_published__list: list[Literal[True, False]] = Depends(bool_list_serializer),
    username: Optional[Username] = Depends(authentication.optional_auth_wrapper),
) -> list[CheatSheetSchema] | None:
    if username is None:
        is_published__list = [True]

    cheat_sheets = cheat_sheet_domain.get_cheat_sheets(
        is_published__list=is_published__list
    )

    send_log_event(
        event_type=EventTypes.CHEAT_SHEET_OPERATION,
        message=f"Fetched all ( {len(cheat_sheets) if cheat_sheets else 0}) cheat sheets",
        user=(username if username else None),
        context={"status": "success", "method": "GET"},
    )

    return cheat_sheets


@router.get("/cheat_sheets/{cheat_sheet_id}")
def get_cheat_sheet_by_id(
    cheat_sheet_id: CheatSheetID,
    username: Optional[Username] = Depends(authentication.optional_auth_wrapper),
) -> CheatSheetSchema | None:
    cheat_sheet = cheat_sheet_domain.get_cheat_sheet(cheat_sheet_id=cheat_sheet_id)

    if username is None and cheat_sheet and cheat_sheet.is_published is False:
        cheat_sheet = None

    send_log_event(
        event_type=EventTypes.CHEAT_SHEET_OPERATION,
        message=f"Fetched single cheat sheet - {cheat_sheet.id if cheat_sheet else 'None'}",
        user=(username if username else None),
        context={"status": "success", "method": "GET"},
    )

    return cheat_sheet


@router.post("/cheat_sheets")
def post_cheat_sheet(
    cheat_sheet_data: UnsavedCheatSheetSchema,
    username: Username = Depends(authentication.auth_wrapper),
) -> MongoInsert:
    created = cheat_sheet_domain.create_cheat_sheet(cheat_sheet_data=cheat_sheet_data)

    send_log_event(
        event_type=EventTypes.CHEAT_SHEET_OPERATION,
        message=f"Created cheat sheet - {created.id}",
        user=(username if username else None),
        context={"status": "success", "method": "POST"},
    )

    return created


@router.patch("/cheat_sheets/{id}")
def patch_cheat_sheet(
    id: str,
    cheat_sheet_data: UpdateCheatSheetSchema,
    username: Username = Depends(authentication.auth_wrapper),
) -> MongoUpdate:
    updated = cheat_sheet_domain.patch_cheat_sheet(
        id=id, cheat_sheet_data=cheat_sheet_data
    )

    send_log_event(
        event_type=EventTypes.CHEAT_SHEET_OPERATION,
        message=f"Updated cheat sheet - {id}",
        user=(username if username else None),
        context={"status": "success", "method": "PATCH"},
    )

    return updated


@router.delete("/cheat_sheets/{id}")
def delete_cheat_sheet(
    id: str, username: Username = Depends(authentication.auth_wrapper)
) -> MongoDelete:
    deleted = cheat_sheet_domain.delete_cheat_sheet(id=id)

    send_log_event(
        event_type=EventTypes.CHEAT_SHEET_OPERATION,
        message=f"deleted cheat sheet - {id}",
        user=(username if username else None),
        context={"status": "success", "method": "DELETE"},
    )

    return deleted
