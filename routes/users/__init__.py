from fastapi import APIRouter

from . import (
    get_users,
    delete_users,
    patch_users,
    post_users
)

router = APIRouter()
router.include_router(get_users.router)
router.include_router(delete_users.router)
router.include_router(post_users.router)
router.include_router(patch_users.router)