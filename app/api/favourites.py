from fastapi import APIRouter

from app.api.dependencies import DBDep
from app.services.favourites import FavouriteService
from app.schemes.favourites import SFavouriteAdd, SFavouriteGet

router = APIRouter(prefix="/favourites", tags=["Избранное"])


@router.get("/user/{user_id}")
async def get_favourites(user_id: int, db: DBDep) -> list[SFavouriteGet]:
    return await FavouriteService(db).get_user_favourites(user_id)


@router.post("/")
async def add_favourite(data: SFavouriteAdd, db: DBDep):
    await FavouriteService(db).add_favourite(data)
    return {"status": "OK"}


@router.delete("/{id}")
async def delete_favourite(id: int, db: DBDep):
    await FavouriteService(db).delete_favourite(id)
    return {"status": "OK"}