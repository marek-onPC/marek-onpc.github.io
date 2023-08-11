from typing import List, Optional
from pydantic import BaseModel


class AuthDetails(BaseModel):
    username: str
    password: str

class User(BaseModel):
    username: str
    password: str
    photo: bytes


class NoteSchema(BaseModel):
    id: Optional[str]
    title: str
    categories: List[str]
    content: str