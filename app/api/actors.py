from fastapi import APIRouter
from app.api.dependencies import DBDep, IsAdminDep
from app.schemes.actors import SActorAdd, SActorGet
from app.services.actors import ActorService
from app.exceptions.actors import ActorNotFoundHTTPError, ActorAlreadyExistsHTTPError

router = APIRouter(prefix="/actors", tags=["Актеры"])


@router.post("/", summary="Создание актера (только админ)")
async def create_actor(actor_data: SActorAdd, db: DBDep, is_admin: IsAdminDep):
    try:
        await ActorService(db).create_actor(actor_data)
    except ActorAlreadyExistsHTTPError:
        raise ActorAlreadyExistsHTTPError()
    return {"status": "OK"}


@router.get("/", summary="Список всех актеров")
async def get_actors(db: DBDep):
    return await ActorService(db).get_all_actors()


@router.get("/{actor_id}", summary="Получение конкретного актера")
async def get_actor(actor_id: int, db: DBDep):
    actor = await ActorService(db).get_actor(actor_id)
    if not actor:
        raise ActorNotFoundHTTPError()
    return actor
