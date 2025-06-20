from enum import StrEnum
from typing import Literal, NewType, Optional

from pydantic import BaseModel

Username = NewType("Username", str)
Password = NewType("Password", str)
HashedPassword = NewType("HashedPassword", str)
CheatSheetID = NewType("CheatSheetID", str)


class AllowedGrandTypes(StrEnum):
    PASSWORD = "password"


class AuthenticationDetails(BaseModel):
    grant_type: AllowedGrandTypes
    username: Username
    password: Password


class User(BaseModel):
    username: Username
    password: HashedPassword


class AuthToken(BaseModel):
    access_token: str
    token_type: Literal["Bearer"]
    expires_in: int
    refresh_token: Optional[str] = None


class AccessToken(BaseModel):
    iss: str
    sub: str
    aud: list[str]
    exp: float
    iat: float


class RefreshToken(BaseModel):
    iss: str
    sub: str
    aud: list[str]
    exp: float
    iat: float


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
