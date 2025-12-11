from pydantic import BaseModel
from typing import Optional


class ResponseUser(BaseModel):
    id: Optional[str] = None
    first_name: str
    last_name: str
    email: Optional[str] = None


class RequestUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class UserUpdateSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
