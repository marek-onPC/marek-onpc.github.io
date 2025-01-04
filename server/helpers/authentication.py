import os
from datetime import datetime, timedelta, timezone
from typing import Optional, Tuple

import jwt
from dotenv import load_dotenv
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext

from schemas import HashedPassword, Password, Token, Username

load_dotenv()

class Authentication:
    security = HTTPBearer()
    optional_security = HTTPBearer(auto_error=False)
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret_key = os.environ["JWT_SECRET"]


    def hash_password(self, password: Password) -> HashedPassword:
        return self.password_context.hash(password)


    def verify_password(self, password: Password, hashed_password: HashedPassword) -> bool:
        return self.password_context.verify(password, hashed_password)


    def encode_jwt(self, user: Username) -> Tuple[Token, datetime]:
        expiry_date = datetime.now(timezone.utc) + timedelta(days=0, hours=8)

        payload = {
            "exp": expiry_date,
            "iat": datetime.now(timezone.utc),
            "sub": user
        }

        return (jwt.encode(payload, self.secret_key, algorithm="HS256"), expiry_date)


    def decode_jwt(self, token: Token) -> Username:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])

            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Signature expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")


    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)) -> Username:
        return self.decode_jwt(auth.credentials)


    def optional_auth_wrapper(self, auth: Optional[HTTPAuthorizationCredentials] = Security(optional_security)) -> Optional[Username]:
        if auth and auth.credentials:
            return self.decode_jwt(auth.credentials)
        else:
            return None
