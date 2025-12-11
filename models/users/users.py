from pydantic import BaseModel
from typing import Optional



class ResponseUser:
    first_name: str
    last_name : str


class RequestUser:
    first_name: str
    last_name : str
    email : str
    password : str


class userUpdateScheme(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


