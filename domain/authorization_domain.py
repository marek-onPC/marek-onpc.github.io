from adapter import authorization_adapter
from fastapi import UploadFile
from schemas.schemas import User
from deepface import DeepFace
from PIL import Image
from io import BytesIO
import numpy

def add_photo(username: str, photo: UploadFile):
    return authorization_adapter.add_photo(username, photo)

def verify_photo(user: User, photo: UploadFile):
    reference = Image.open(BytesIO(user.photo))
    to_verify = Image.open(BytesIO(photo.file.read()))

    try:
        return DeepFace.verify(img1_path=numpy.array(reference), img2_path=numpy.array(to_verify))["verified"]
    except ValueError:
        return False
