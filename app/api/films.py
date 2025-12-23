from fastapi import APIRouter

from app.api.dependencies import DBDep, IsAdminDep
from app.schemes.films import SFilmAdd, SFilmGet
from app.services.films import FilmService
from app.exceptions.films import FilmNotFoundError, FilmNotFoundHTTPError

router = APIRouter(prefix="/films", tags=["Фильмы"])


@router.get("/")
async def get_films(db: DBDep) -> list[SFilmGet]:
    return await FilmService(db).get_films()


@router.get("/{film_id}")
async def get_film(film_id: int, db: DBDep) -> SFilmGet:
    try:
        return await FilmService(db).get_film(film_id)
    except FilmNotFoundError:
        raise FilmNotFoundHTTPError


@router.post("/")
async def create_film(
    film_data: SFilmAdd,
    db: DBDep,
    is_admin: IsAdminDep,
):
    await FilmService(db).create_film(film_data)
    return {"status": "OK"}


@router.put("/{film_id}")
async def edit_film(
    film_id: int,
    film_data: SFilmAdd,
    db: DBDep,
    is_admin: IsAdminDep,
):
    try:
        await FilmService(db).edit_film(film_id, film_data)
    except FilmNotFoundError:
        raise FilmNotFoundHTTPError
    return {"status": "OK"}


@router.delete("/{film_id}")
async def delete_film(
    film_id: int,
    db: DBDep,
    is_admin: IsAdminDep,
):
    try:
        await FilmService(db).delete_film(film_id)
    except FilmNotFoundError:
        raise FilmNotFoundHTTPError
    return {"status": "OK"}
