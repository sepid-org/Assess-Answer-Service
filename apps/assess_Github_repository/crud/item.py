from apps.assess_Github_repository.models.item import ItemModel
from apps.assess_Github_repository.schemas.item import ItemCreate
from apps.db.database import mongodb
from bson import ObjectId


async def create_item(item: ItemCreate):
    item_dict = item.model_dump()
    result = await mongodb.db["items"].insert_one(item_dict)
    created_item = await mongodb.db["items"].find_one({"_id": result.inserted_id})
    return ItemModel(**created_item)


async def list_items():
    items = []
    async for item in mongodb.db["items"].find():
        items.append(ItemModel(**item))
    return items


async def get_item(item_id: str):
    item = await mongodb.db["items"].find_one({"_id": ObjectId(item_id)})
    if item is None:
        return None
    return ItemModel(**item)


async def update_item(item_id: str, item: ItemCreate):
    await mongodb.db["items"].update_one({"_id": ObjectId(item_id)}, {"$set": item.model_dump()})
    updated_item = await mongodb.db["items"].find_one({"_id": ObjectId(item_id)})
    if updated_item is None:
        return None
    return ItemModel(**updated_item)


async def delete_item(item_id: str):
    result = await mongodb.db["items"].delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count
