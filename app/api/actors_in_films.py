from fastapi import APIRouter

from app.api.dependencies import DBDep, IsAdminDep
from app.services.actors_in_films import ActorInFilmService
from app.schemes.actors_in_films import SActorInFilmAdd

router = APIRouter(prefix="/actors-in-films", tags=["Актёры в фильмах"])


@router.get("/film/{film_id}")
async def get_actors_for_film(film_id: int, db: DBDep):
    return await ActorInFilmService(db).get_actors_for_film(film_id)


@router.post("/")
async def add_actor_to_film(
    data: SActorInFilmAdd,
    db: DBDep,
    is_admin: IsAdminDep,
):
    await ActorInFilmService(db).add_actor(data)
    return {"status": "OK"}


@router.delete("/{id}")
async def delete_actor_from_film(
    id: int,
    db: DBDep,
    is_admin: IsAdminDep,
):
    await ActorInFilmService(db).delete_actor(id)
    return {"status": "OK"}
