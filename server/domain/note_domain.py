from schemas import schemas
from adapter import note_adapter


def get_notes():
    return note_adapter.get_notes()


def get_note_by_id(note_id: str):
    return note_adapter.get_note_by_id(note_id=note_id)


def post_new_note(note_data: schemas.NoteSchema):
    return note_adapter.post_new_note(note_data=note_data)


def update_note(note_data: schemas.NoteSchema):
    return note_adapter.update_note(note_data=note_data)
