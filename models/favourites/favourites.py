from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class RequestFavourites(BaseModel):
    id: UUID
    created_at: str
    prompt_id: str


class ResponseFavourites(BaseModel):
    id: UUID
    created_at: str
    prompt_id: str



class FavouritesUpdateSchema(BaseModel):
    id: Optional[UUID] = None
    created_at: Optional[str] = None
    prompt_id: Optional[str] = None

  
