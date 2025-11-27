from fastapi import HTTPException, APIRouter
from supabaseClient import SupabaseClient
from models.prompts import RequestPrompt, ResponsePrompt
from typing import List

client = SupabaseClient()

router = APIRouter()


@router.post("/prompts", response_model=List[ResponsePrompt])
def create_prompt(prompt: RequestPrompt):
    try:
        data = client.fetch('prompts')
        print(data)
        return data
        # return {"success": True, "data": data, "count": len(data)}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching prompts: {str(e)}")
