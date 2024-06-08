from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: str


class UserResponse(UserCreate):
    id: str
