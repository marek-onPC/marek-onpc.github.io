import os
from datetime import datetime, timezone
from typing import Optional

import jwt
from dotenv import load_dotenv
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext

from schemas import (
    AccessToken,
    AuthToken,
    HashedPassword,
    Password,
    RefreshToken,
    Username,
)

load_dotenv()


class Authentication:
    security = HTTPBearer()
    optional_security = HTTPBearer(auto_error=False)
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    algorithm = "HS256"
    secret_key = os.environ["JWT_SECRET"]
    issuer = os.environ["JWT_ISSUER"]
    audience = os.environ["JWT_AUDIENCE"]

    def hash_password(self, password: Password) -> HashedPassword:
        return HashedPassword(self.password_context.hash(password))

    def verify_password(
        self, password: Password, hashed_password: HashedPassword
    ) -> bool:
        return self.password_context.verify(password, hashed_password)

    def encode_jwt(self, user: Username) -> AuthToken:
        now = datetime.now(timezone.utc)

        raw_access_token = AccessToken(
            iss=self.issuer,
            sub=user,
            aud=[self.audience],
            exp=now.timestamp() + 3600,  # 1 hour
            iat=now.timestamp(),
        )

        raw_refresh_token = RefreshToken(
            iss=self.issuer,
            sub=user,
            aud=[self.audience],
            exp=now.timestamp() + 28800,  # 8 hours
            iat=now.timestamp(),
        )

        access_token = jwt.encode(
            raw_access_token.model_dump(),
            self.secret_key,
            algorithm=self.algorithm,
        )

        refresh_token = jwt.encode(
            raw_refresh_token.model_dump(),
            self.secret_key,
            algorithm=self.algorithm,
        )

        auth_token = AuthToken(
            access_token=access_token,
            token_type="Bearer",
            expires_in=3600,
            refresh_token=refresh_token,
        )

        return auth_token

    def decode_jwt(self, token: str) -> Username:
        try:
            payload = jwt.decode(
                jwt=token,
                key=self.secret_key,
                algorithms=[self.algorithm],
                audience=[self.audience],
            )
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Signature expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")

    def auth_wrapper(
        self, auth: HTTPAuthorizationCredentials = Security(security)
    ) -> Username:
        return self.decode_jwt(auth.credentials)

    def optional_auth_wrapper(
        self, auth: Optional[HTTPAuthorizationCredentials] = Security(optional_security)
    ) -> Optional[Username]:
        if auth and auth.credentials:
            return self.decode_jwt(auth.credentials)
        else:
            return None
