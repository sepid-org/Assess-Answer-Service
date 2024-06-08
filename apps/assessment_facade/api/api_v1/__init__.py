from fastapi import APIRouter
from apps.assessment_facade.api.api_v1.endpoints import main

api_router = APIRouter()
api_router.include_router(main.router, prefix="/assess", tags=["assessment"])
