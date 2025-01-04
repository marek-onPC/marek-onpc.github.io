from typing import Any, Optional, TypeVar

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
    expiry : float


class CheatSheetContent(BaseModel):
    subtitle: str
    content: str


class UnsavedCheatSheetSchema(BaseModel):
    title: str
    language: Optional[str] = None
    is_published: bool = False


class UpdateCheatSheetSchema(UnsavedCheatSheetSchema):
    cards: Optional[list[CheatSheetContent]] = None


class CheatSheetSchema(UpdateCheatSheetSchema):
    id: CheatSheetID


class MongoInsert(BaseModel):
    id: str


class MongoUpdate(BaseModel):
    acknowledged: bool


class MongoDelete(BaseModel):
    acknowledged: bool
