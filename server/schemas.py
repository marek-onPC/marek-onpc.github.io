from typing import Optional, TypeVar
from pydantic import BaseModel

Username = TypeVar("Username", bound=str)
Password = TypeVar("Password", bound=str)
HashedPassword = TypeVar("HashedPassword", bound=str)
Token = TypeVar("Token", bound=str)
CheatSheetID = TypeVar("CheatSheetID", bound=str)


class AuthDetails(BaseModel):
    username: Username
    password: Password


class User(BaseModel):
    username: Username
    password: HashedPassword


class LoginToken(BaseModel):
    token: Token


class UnsavedCheatSheetSchema(BaseModel):
    title: str
    category: Optional[list[str]] = None
    is_published: bool = False


class UpdateCheatSheetSchema(UnsavedCheatSheetSchema):
    content: Optional[str] = None
    is_published: bool


class CheatSheetSchema(UpdateCheatSheetSchema):
    id: CheatSheetID
