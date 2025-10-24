from fastapi import APIRouter

from . import (
    get_users
)

router = APIRouter()
router.include_router(get_users.router)
# router.include_router(get_users.router)
# router.include_router(get_users.router)
