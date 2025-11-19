from supabaseClient import SupabaseClient
from fastapi import HTTPException, APIRouter

client = SupabaseClient()

router = APIRouter()