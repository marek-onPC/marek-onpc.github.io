from typing import List, Optional
from pydantic import BaseModel
from fastapi import UploadFile, File, Form

class AuthDetails(BaseModel):
    username: str = Form(...)
    password: str = Form(...)

class User(BaseModel):
    username: str
    password: str
    photo: Optional[UploadFile]


class NoteSchema(BaseModel):
    id: Optional[str]
    title: str
    categories: List[str]
    content: str