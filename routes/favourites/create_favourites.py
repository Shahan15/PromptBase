from fastapi import HTTPException, APIRouter, status
from supabaseClient import SupabaseClient
from models.favourites import RequestFavourites, ResponseFavourites
from typing import List

client = SupabaseClient()

router = APIRouter()

@router.post("/favourites", response_model=List[ResponseFavourites], status_code=status.HTTP_201_CREATED)
def create_favourites(favourite: RequestFavourites):
    try:
        favourite_data = favourite.model_dump()
        created_favourites = client.insert(table='favourites', data=favourite_data)
        return created_favourites
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating favourite: {str(e)}"
        )
