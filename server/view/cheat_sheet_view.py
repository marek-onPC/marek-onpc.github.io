from typing import Literal, Optional
from fastapi import Depends, APIRouter, HTTPException
from helpers.authentication import Authentication
from domain import cheat_sheet_domain
from schemas import CheatSheetID, UnsavedCheatSheetSchema, UpdateCheatSheetSchema, Username
from helpers.serializers import bool_list_serializer


router = APIRouter(prefix="/api")
authentication = Authentication()


@router.get("/cheat_sheets")
def cheat_sheets(
    is_published__list: list[Literal[True, False]] = Depends(bool_list_serializer),
    username: Optional[Username] = Depends(authentication.optional_auth_wrapper),
):
    if username is None:
        is_published__list = [True]
    return cheat_sheet_domain.get_cheat_sheets(is_published__list=is_published__list)


@router.get("/cheat_sheets/{cheat_sheet_id}")
def get_cheat_sheet_by_id(cheat_sheet_id: CheatSheetID):
    return cheat_sheet_domain.get_cheat_sheet(cheat_sheet_id=cheat_sheet_id)


@router.post("/cheat_sheets")
def post_cheat_sheet(cheat_sheet_data: UnsavedCheatSheetSchema, username: Username = Depends(authentication.auth_wrapper)) -> str:
    if username:
        return cheat_sheet_domain.create_cheat_sheet(cheat_sheet_data=cheat_sheet_data)
    else:
        raise HTTPException(status_code=401, detail="Non authenticated")


@router.patch("/cheat_sheets/{id}")
def patch_cheat_sheet(id: str, cheat_sheet_data: UpdateCheatSheetSchema, username: Username = Depends(authentication.auth_wrapper)):
    if username:
        return cheat_sheet_domain.patch_cheat_sheet(id=id, cheat_sheet_data=cheat_sheet_data)
    else:
        raise HTTPException(status_code=401, detail="Non authenticated")


@router.delete("/cheat_sheets/{id}")
def delete_cheat_sheet(id: str, username: Username = Depends(authentication.auth_wrapper)):
    if username:
        return cheat_sheet_domain.delete_cheat_sheet(id=id)
    else:
        raise HTTPException(status_code=401, detail="Non authenticated")
