from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    role: int


class UserCreate(UserBase):
    role: str


class User(UserBase):
    id: Optional[int]
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
