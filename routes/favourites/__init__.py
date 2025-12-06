from fastapi import APIRouter

from . import(
    delete_favourite
)

router = APIRouter()
router.include_router(delete_favourite.router)