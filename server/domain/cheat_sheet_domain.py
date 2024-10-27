from schemas import CheatSheetID, CheatSheetSchema, UnsavedCheatSheetSchema
from adapter import cheat_sheet_adapter


def get_cheat_sheets():
    return cheat_sheet_adapter.get_cheat_sheets()


def get_cheat_sheet(cheat_sheet_id: CheatSheetID):
    return cheat_sheet_adapter.get_cheat_sheet(cheat_sheet_id=cheat_sheet_id)


def create_cheat_sheet(cheat_sheet_data: UnsavedCheatSheetSchema) -> str:
    return cheat_sheet_adapter.create_cheat_sheet(cheat_sheet_data=cheat_sheet_data)


def patch_cheat_sheet(id: str, cheat_sheet_data: CheatSheetSchema):
    return cheat_sheet_adapter.patch_cheat_sheet(id=id, cheat_sheet_data=cheat_sheet_data)
