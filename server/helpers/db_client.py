from typing import Self

from pymongo import MongoClient
from pymongo.database import Database


class DatabaseClient:
    _INSTANCE: Self | None = None

    def __new__(cls: type[Self], uri: str, name: str) -> Self:
        if cls._INSTANCE is None:
            cls._INSTANCE = super(DatabaseClient, cls).__new__(cls)
        return cls._INSTANCE

    def __init__(self: Self, uri: str, name: str) -> None:
        if getattr(self, "_initialized", False):
            return

        self._initialized = True
        self.uri = uri
        self.name = name

    def connection(self) -> Database:
        client: MongoClient = MongoClient(
            self.uri, tls=True, tlsAllowInvalidCertificates=True
        )
        database = client[self.name]

        return database
