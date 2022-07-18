from typing import Dict, Optional
from pydantic import BaseModel


class AuthDetails(BaseModel):
    username: str
    password: str


class NoteSchema(BaseModel):
    _id: Optional[str]
    title: str
    categories: Dict[str, str]
    content: str