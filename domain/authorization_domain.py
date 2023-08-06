from adapter import authorization_adapter
from fastapi import UploadFile

def add_photo(username: str, photo: UploadFile):
    return authorization_adapter.add_photo(username, photo)
