from fastapi import HTTPException, APIRouter, status
from supabaseClient import SupabaseClient
from models.prompts import RequestPrompt, ResponsePrompt
from typing import List
from GeminiClient import GeminiClient

geminiClient = GeminiClient()
client = SupabaseClient()


# {
#   "original_prompt": "I want to create a website about cars",
#   "is_private": true,
#   "tags": "website,html",
#   "user_id": "01c462b4-3751-4d1b-8034-c507e9b6205e"
# }


router = APIRouter()

@router.post("/prompts", response_model=List[ResponsePrompt], status_code=status.HTTP_201_CREATED)
def create_prompt(prompt: RequestPrompt):
    try:
        prompt_data = prompt.model_dump()
        optimised_prompt = geminiClient.generateOptimisedPrompt(prompt_data["original_prompt"])
        prompt_data["optimised_prompt"] = optimised_prompt
        created_prompt = client.insert(table='prompts', data=prompt_data)
        return created_prompt
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating prompt: {str(e)}"
        )
