from fastapi import APIRouter
from app.api.dependencies import DBDep
from app.schemes.favourites import SFavouriteAdd, SFavouriteGet
from app.services.favourites import FavouriteService
from app.exceptions.favourites import FavouriteNotFoundHTTPError, FavouriteAlreadyExistsHTTPError

router = APIRouter(prefix="/favourites", tags=["Избранное"])


@router.post("/", summary="Добавление в избранное")
async def add_favourite(fav_data: SFavouriteAdd, db: DBDep):
    try:
        await FavouriteService(db).add_favourite(fav_data)
    except FavouriteAlreadyExistsHTTPError:
        raise FavouriteAlreadyExistsHTTPError()
    return {"status": "OK"}


@router.get("/", summary="Список всех избранных")
async def get_favourites(db: DBDep):
    return await FavouriteService(db).get_all_favourites()


@router.get("/{fav_id}", summary="Получение конкретного избранного")
async def get_favourite(fav_id: int, db: DBDep):
    fav = await FavouriteService(db).get_favourite(fav_id)
    if not fav:
        raise FavouriteNotFoundHTTPError()
    return fav
