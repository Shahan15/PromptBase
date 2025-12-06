from fastapi import APIRouter

from . import (
    get_prompts,
    create_prompt
)

router = APIRouter()
router.include_router(get_prompts.router)
router.include_router(create_prompt.router)
