from fastapi import HTTPException, APIRouter, status
from supabaseClient import SupabaseClient
from models.prompts import RequestPrompt, ResponsePrompt
from typing import List

client = SupabaseClient()

router = APIRouter()

@router.post("/prompts", response_model=List[ResponsePrompt], status_code=status.HTTP_201_CREATED)
def create_prompt(prompt: RequestPrompt):
    try:
        prompt_data = prompt.model_dump()
        created_prompt = client.insert(table='prompts', data=prompt_data)
        return created_prompt
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating prompt: {str(e)}"
        )
