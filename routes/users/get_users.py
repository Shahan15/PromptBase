from supabase import create_client, Client
from fastapi import HTTPException, APIRouter
from dotenv import load_dotenv
from supabaseClient import SupabaseClient
import os


client = SupabaseClient()

router = APIRouter()


@router.get("/users")
def get_users():
    try:

        data = client.fetch('users')
        return {"success": True, "data": data, "count": len(data)}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching users: {str(e)}")
