from supabaseClient import SupabaseClient
from fastapi import HTTPException, APIRouter, status
from uuid import UUID
from models.favourites import FavouritesUpdateSchema

client = SupabaseClient()

router = APIRouter()

@router.patch('/favourites/{favourite_id}', status_code=status.HTTP_200_OK)
def update_favourite(favourite_id: UUID, favouriteUpdate: FavouritesUpdateSchema):
    try:
        update_data = favouriteUpdate.model_dump(exclude_unset=True)

        if not update_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='No fields provided to update'
            )

        updates = client.update(
            table='favourites',
            filters={
                'id': favourite_id,
            },
            updates=update_data
        )

        if not updates:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Favourite with id {favourite_id} could not be found'
            )

        return updates

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Error updating requested fields: {str(e)}'
        )
