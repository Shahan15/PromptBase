from fastapi import APIRouter

from . import (
    get_prompts,
    create_prompt,
    delete_prompt,
    patch_prompts
)

router = APIRouter()
router.include_router(get_prompts.router)
router.include_router(create_prompt.router)
router.include_router(delete_prompt.router)
router.include_router(patch_prompts.router)
