from apps.assess_Github_repository.models.user import UserModel
from apps.assess_Github_repository.schemas.user import UserCreate
from apps.db.database import mongodb
from bson import ObjectId


async def create_user(user: UserCreate):
    user_dict = user.model_dump()
    result = await mongodb.db["users"].insert_one(user_dict)
    created_user = await mongodb.db["users"].find_one({"_id": result.inserted_id})
    return UserModel(**created_user)


async def list_users():
    users = []
    async for user in mongodb.db["users"].find():
        users.append(UserModel(**user))
    return users


async def get_user(user_id: str):
    user = await mongodb.db["users"].find_one({"_id": ObjectId(user_id)})
    if user is None:
        return None
    return UserModel(**user)


async def update_user(user_id: str, user: UserCreate):
    await mongodb.db["users"].update_one({"_id": ObjectId(user_id)}, {"$set": user.model_dump()})
    updated_user = await mongodb.db["users"].find_one({"_id": ObjectId(user_id)})
    if updated_user is None:
        return None
    return UserModel(**updated_user)


async def delete_user(user_id: str):
    result = await mongodb.db["users"].delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count
