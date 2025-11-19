from supabaseClient import SupabaseClient
from fastapi import HTTPException, APIRouter,status
from uuid import UUID  # Import the UUID type

client = SupabaseClient()

router = APIRouter()

#DELETE A PROMPT
@router.delete('/prompts/{prompt_id}')
def delete_prompt(prompt_id : UUID):
    #Deletes prompt via its prompt id
    try: 
        result = client.delete(
            table = 'prompts',
            pk_id = prompt_id,

        )
    
        if not result or len(result) == 0: 
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Prompt with Prompt_id:{prompt_id} not found'
            )
        return
    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Error deleting Prompt : {str(e)}'
        )
    
#DELETE A FAVOURITE PROMPT
router.delete('/favourites/{favourite_id}')
def delete_favourite(favourite_id : UUID):
    try:
        result = client.delete(
            table = 'favourites',
            pk_id= favourite_id
        )

        if not result or len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Could not find favourite with favourite id : {favourite_id}'
            )
        return
    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Error deleting favourite: {str(e)}'
        )