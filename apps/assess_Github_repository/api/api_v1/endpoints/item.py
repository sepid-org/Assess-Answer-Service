from fastapi import APIRouter, HTTPException
from typing import List
from apps.assess_Github_repository.schemas.item import ItemCreate, ItemResponse
from apps.assess_Github_repository.crud import item as crud_item

router = APIRouter()


@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate):
    return await crud_item.create_item(item)


@router.get("/", response_model=List[ItemResponse])
async def list_items():
    return await crud_item.list_items()


@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: str):
    item = await crud_item.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(item_id: str, item: ItemCreate):
    updated_item = await crud_item.update_item(item_id, item)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item


@router.delete("/{item_id}", response_model=dict)
async def delete_item(item_id: str):
    deleted_count = await crud_item.delete_item(item_id)
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"}
