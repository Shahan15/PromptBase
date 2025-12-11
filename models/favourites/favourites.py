from pydantic import BaseModel


class RequestFavourites(BaseModel):
    id : str
    created_at : str
    prompt_id : str

class ResponseFavourites(BaseModel):
    id : str
    created_at : str
    prompt_id : str

class favouritesUpdateSchema(BaseModel):
    id : str
    created_at : str
    prompt_id : str
