import os
import jwt
from dotenv import load_dotenv
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from datetime import datetime, timedelta
from passlib.context import CryptContext

load_dotenv()

class Authentication():
    security = HTTPBearer()
    passwordContext = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secretKEY = os.environ["JWT_SECRET"]

    def hashPassword(self, password):
        return self.passwordContext.hash(password)

    def verifyPassword(self, password, hashedPassword):
        return self.passwordContext.verify(password, hashedPassword)

    def encodeJWT(self, user):
        payload = {
            "exp": datetime.utcnow() + timedelta(days=0, minutes=5),
            "iat": datetime.utcnow(),
            "sub": user
        }

        return jwt.encode(payload, self.secretKEY, algorithm="HS256")

    def decodeJWT(self, token):
        try:
            payload = jwt.decode(token, self.secretKEY, algorithms=["HS256"])

            return payload['sub']
        except jwt.ExpiredSignatureError:
            return HTTPException(status_code=401, detail="Signature expired")
        except jwt.InvalidTokenError:
            return HTTPException(status_code=401, detail="Invalid token")

    def authWrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decodeJWT(auth.credentials)