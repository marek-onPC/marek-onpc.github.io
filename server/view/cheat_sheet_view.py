from typing import Literal, Optional

from fastapi import APIRouter, Depends

from domain import cheat_sheet_domain
from helpers.authentication import Authentication
from helpers.serializers import bool_list_serializer
from schemas import (
    CheatSheetID,
    CheatSheetSchema,
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

    return cheat_sheet_domain.get_cheat_sheets(is_published__list=is_published__list)


@router.get("/cheat_sheets/{cheat_sheet_id}")
def get_cheat_sheet_by_id(
    cheat_sheet_id: CheatSheetID,
    username: Optional[Username] = Depends(authentication.optional_auth_wrapper),
) -> CheatSheetSchema | None:
    cheat_sheet = cheat_sheet_domain.get_cheat_sheet(cheat_sheet_id=cheat_sheet_id)

    if username is None and cheat_sheet and cheat_sheet.is_published is False:
        return None

    return cheat_sheet


@router.post("/cheat_sheets")
def post_cheat_sheet(
    cheat_sheet_data: UnsavedCheatSheetSchema,
    _: Username = Depends(authentication.auth_wrapper),
) -> MongoInsert:
    return cheat_sheet_domain.create_cheat_sheet(cheat_sheet_data=cheat_sheet_data)


@router.patch("/cheat_sheets/{id}")
def patch_cheat_sheet(
    id: str,
    cheat_sheet_data: UpdateCheatSheetSchema,
    _: Username = Depends(authentication.auth_wrapper),
) -> MongoUpdate:
    return cheat_sheet_domain.patch_cheat_sheet(
        id=id, cheat_sheet_data=cheat_sheet_data
    )


@router.delete("/cheat_sheets/{id}")
def delete_cheat_sheet(
    id: str, _: Username = Depends(authentication.auth_wrapper)
) -> MongoDelete:
    return cheat_sheet_domain.delete_cheat_sheet(id=id)
