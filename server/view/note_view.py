from fastapi import Depends, APIRouter, HTTPException
from server.auth.authentication import Authentication
from server.domain import note_domain
from server.schemas.schemas import NoteSchema


router = APIRouter(prefix="/api")
authentication = Authentication()


@router.get("/notes")
def notes():
    return note_domain.get_notes()


@router.get("/note/{note_id}")
def get_note_by_id(note_id: str):
    return note_domain.get_note_by_id(note_id=note_id)


@router.post("/note")
def post_note(note_data: NoteSchema, username = Depends(authentication.auth_wrapper)):
    if username:
        if note_data.id == "":
            return note_domain.post_new_note(note_data=note_data)
        else:
            return note_domain.update_note(note_data=note_data)
    else:
        raise HTTPException(status_code=401, detail="Non authenticated")
