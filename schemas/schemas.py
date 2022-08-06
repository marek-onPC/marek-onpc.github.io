from typing import Dict, List, Optional
from pydantic import BaseModel


class AuthDetails(BaseModel):
    username: str
    password: str


class NoteSchema(BaseModel):
    id: Optional[str]
    title: str
    categories: List[str]
    content: str