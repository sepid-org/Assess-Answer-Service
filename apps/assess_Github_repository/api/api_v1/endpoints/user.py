from fastapi import APIRouter, HTTPException
from typing import List
from apps.assess_Github_repository.schemas.user import UserCreate, UserResponse
from apps.assess_Github_repository.crud import user as crud_user

router = APIRouter()


@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    return await crud_user.create_user(user)


@router.get("/", response_model=List[UserResponse])
async def list_users():
    return await crud_user.list_users()


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    user = await crud_user.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user: UserCreate):
    updated_user = await crud_user.update_user(user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/{user_id}", response_model=dict)
async def delete_user(user_id: str):
    deleted_count = await crud_user.delete_user(user_id)
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}
