from typing import Self

from pymongo import MongoClient
from pymongo.collection import Collection


class DatabaseClient:
    _INSTANCE: Self | None = None

    def __new__(cls: type[Self], uri: str, name: str, collection: str) -> Self:
        if cls._INSTANCE is None:
            cls._INSTANCE = super(DatabaseClient, cls).__new__(cls)
        return cls._INSTANCE

    def __init__(self: Self, uri: str, name: str, collection: str) -> None:
        if getattr(self, "_initialized", False):
            return

        self._initialized = True
        self.uri = uri
        self.name = name
        self.collection = collection

    def connection(self) -> Collection:
        client: MongoClient = MongoClient(
            self.uri, tls=True, tlsAllowInvalidCertificates=True
        )
        database = client[self.name]
        collection = database[self.collection]

        return collection
