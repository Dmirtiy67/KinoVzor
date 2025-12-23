from fastapi import APIRouter
from app.api.dependencies import DBDep, IsAdminDep
from app.schemes.films import SFilmAdd, SFilmGet
from app.services.films import FilmService
from app.exceptions.films import FilmNotFoundHTTPError, FilmAlreadyExistsHTTPError

router = APIRouter(prefix="/films", tags=["Фильмы"])


@router.post("/", summary="Создание фильма (только админ)")
async def create_film(film_data: SFilmAdd, db: DBDep, is_admin: IsAdminDep):
    try:
        await FilmService(db).create_film(film_data)
    except FilmAlreadyExistsHTTPError:
        raise FilmAlreadyExistsHTTPError()
    return {"status": "OK"}


@router.get("/", summary="Список всех фильмов")
async def get_films(db: DBDep):
    return await FilmService(db).get_all_films()


@router.get("/{film_id}", summary="Получение конкретного фильма")
async def get_film(film_id: int, db: DBDep):
    film = await FilmService(db).get_film(film_id)
    if not film:
        raise FilmNotFoundHTTPError()
    return film
