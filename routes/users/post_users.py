from supabaseClient import SupabaseClient
from fastapi import HTTPException, APIRouter,status
from pydantic import BaseModel

client = SupabaseClient()

router = APIRouter()

class UserCreateSchema(BaseModel):
    first_name : str
    last_name : str
    email : str
    password : str

#Sending data to database to update/create
@router.post('/',status_code=status.HTTP_201_CREATED)
def create_user(new_user : UserCreateSchema):
    #CREATING A NEW USER 
    try: 
        user_data = new_user.model_dump()
        created_user = client.insert(table='users',data=user_data)
        return created_user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating user: {str(e)}"
        )