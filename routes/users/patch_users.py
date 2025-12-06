from supabaseClient import SupabaseClient
from fastapi import HTTPException, APIRouter, status
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

client = SupabaseClient()

router = APIRouter()


class UserUpdateScheme(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class promptsUpdateSchema(BaseModel):
    is_private: Optional[bool] = None
    tags: Optional[str] = None


@router.patch('/users/{user_id}', status_code=status.HTTP_200_OK)
def update_users_profile(user_id: UUID, userUpdate: UserUpdateScheme):
    # PARTIAL UPDATE
    try:
        # Ensure dict only contains fields the user actually sends. ignores None values
        update_data = userUpdate.model_dump(exclude_unset=True)

        # if not fields are provided
        if not update_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='No fields provided to update'
            )

        updates = client.update(
            table='users',
            filters={
                'id': user_id
            },
            updates=update_data
        )

        # if user cannot be found
        if not updates:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Could not find user with user ID:{user_id}'
            )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Error updating requested fields {str(e)}'
        )


@router.patch('/prompts/{prompt_id}', status_code=status.HTTP_200_OK)
def update_prompt(prompt_id: UUID, promptUpdate: promptsUpdateSchema):
    try:
        update_data = promptUpdate.model_dump(exclude_unset=True)

        if not update_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='No fields provided to update'
            )

        updates = client.update(
            table='prompts',
            filters={
                'id': prompt_id,
            },
            updates=update_data
        )

        if not updates:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'prompt with id : {prompt_id} could not be found'
            )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Error updating requested fields {str(e)}'
        )
