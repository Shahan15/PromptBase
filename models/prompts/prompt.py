from pydantic import BaseModel
from typing import Optional


# {
#       "id": "c58ef35d-0e3d-4173-92b3-ee19bd6fbf0b",
#       "created_at": "2025-10-17T23:46:57.37204+00:00",
#       "original_prompt": "This is a test prompt 2",
#       "optimised_prompt": "This is a test opt prompt the second",
#       "is_private": false,
#       "tags": "tagsatagatagstags",
#       "user_id": "01c462b4-3751-4d1b-8034-c507e9b6205e"
#     }


class RequestPrompt(BaseModel):
    original_prompt: str
    optimised_prompt: str
    is_private: bool
    tags: str
    user_id: str


class ResponsePrompt(BaseModel):
    id: str
    created_at: str
    original_prompt: str
    optimised_prompt: str
    is_private: bool
    tags: str
    user_id: str

class promptsUpdateSchema(BaseModel):
    is_private: Optional[bool] = None
    tags: Optional[str] = None
