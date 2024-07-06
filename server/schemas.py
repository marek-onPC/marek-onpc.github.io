from enum import StrEnum
from typing import Optional
from pydantic import BaseModel


class AuthDetails(BaseModel):
    username: str
    password: str


class User(BaseModel):
    username: str
    password: str


class ProjectType(StrEnum):
    main = "MAIN"
    minor = "MINOR"


class ProjectSchema(BaseModel):
    id: Optional[str]
    title: str
    project_type: ProjectType
    content: str
