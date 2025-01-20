from pymongo import MongoClient
from pymongo.collection import Collection


class DatabaseClient:
    def __init__(self, uri: str, name: str, collection: str) -> None:
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
