from fastapi import APIRouter
from app.api.dependencies import DBDep, IsAdminDep
from app.schemes.actors_in_films import SActorInFilmAdd
from app.services.actors_in_films import ActorsInFilmsService
from app.exceptions.actors_in_films import ActorInFilmNotFoundHTTPError, ActorInFilmAlreadyExistsHTTPError

router = APIRouter(prefix="/actors-in-films", tags=["Актеры в фильмах"])


@router.post("/", summary="Добавление актера к фильму (только админ)")
async def add_actor_in_film(data: SActorInFilmAdd, db: DBDep, is_admin: IsAdminDep):
    try:
        await ActorsInFilmsService(db).add_actor_in_film(data)
    except ActorInFilmAlreadyExistsHTTPError:
        raise ActorInFilmAlreadyExistsHTTPError()
    return {"status": "OK"}


@router.get("/", summary="Список всех актеров в фильмах")
async def get_actors_in_films(db: DBDep):
    return await ActorsInFilmsService(db).get_all()
