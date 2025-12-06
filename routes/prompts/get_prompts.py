from fastapi import HTTPException, APIRouter
from supabaseClient import SupabaseClient
from models.prompts import ResponsePrompt
from typing import List

client = SupabaseClient()

router = APIRouter()


@router.get("/prompts", response_model=List[ResponsePrompt])
def get_prompts():
    try:
        data = client.fetch('prompts')
        print(data)
        return data
        # return {"success": True, "data": data, "count": len(data)}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching prompts: {str(e)}")
