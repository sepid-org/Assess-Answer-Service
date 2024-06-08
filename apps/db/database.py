from motor.motor_asyncio import AsyncIOMotorClient
from apps.core.config import settings


class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]


# Initialize the MongoDB client
mongodb = MongoDB(settings.MONGO_URI, settings.DB_NAME)
