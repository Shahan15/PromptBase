from fastapi import APIRouter

from . import(
    delete_favourite,
    get_favourites
)

router = APIRouter()
router.include_router(delete_favourite.router)
router.include_router(get_favourites.router)