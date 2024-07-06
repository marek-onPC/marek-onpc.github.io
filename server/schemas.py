from enum import StrEnum
from typing import TypeVar
from pydantic import BaseModel

Username = TypeVar("Username", bound=str)
Password = TypeVar("Password", bound=str)
HashedPassword = TypeVar("HashedPassword", bound=str)
Token = TypeVar("Token", bound=str)
ProjectID = TypeVar("ProjectID", bound=str)


class AuthDetails(BaseModel):
    username: Username
    password: Password


class User(BaseModel):
    username: Username
    password: HashedPassword


class LoginToken(BaseModel):
    token: Token


class ProjectType(StrEnum):
    main = "MAIN"
    minor = "MINOR"


class UnsavedProjectSchema(BaseModel):
    title: str
    project_type: ProjectType
    content: str


class ProjectSchema(BaseModel):
    id: ProjectID
    title: str
    project_type: ProjectType
    content: str
