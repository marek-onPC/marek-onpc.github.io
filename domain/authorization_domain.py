from adapter import authorization_adapter
from fastapi import UploadFile
from schemas.schemas import User
from deepface import DeepFace
from PIL import Image
from io import BytesIO
import numpy
import base64

def add_photo(username: str, photo: UploadFile):
    return authorization_adapter.add_photo(username, photo)

def verify_photo(user: User, photo: str):
    reference = Image.open(BytesIO(user.photo)).convert('RGB')
    to_verify = Image.open(BytesIO(base64.b64decode(photo.split(',')[1]))).convert('RGB')

    try:
        return DeepFace.verify(img1_path=numpy.array(reference), img2_path=numpy.array(to_verify), model_name="Facenet")["verified"]
    except ValueError:
        return False
