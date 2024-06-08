from fastapi import APIRouter
from apps.assess_Github_repository.api.api_v1.endpoints import item, user

api_router = APIRouter()
api_router.include_router(item.router, prefix="/items", tags=["items"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
