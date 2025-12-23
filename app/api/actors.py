from fastapi import APIRouter

from app.api.dependencies import DBDep, IsAdminDep
from app.schemes.actors import SActorAdd, SActorGet
from app.services.actors import ActorService
from app.exceptions.actors import (
    ActorAlreadyExistsError,
    ActorAlreadyExistsHTTPError,
    ActorNotFoundError,
    ActorNotFoundHTTPError,
)

router = APIRouter(prefix="/actors", tags=["Актёры"])


@router.get("/", summary="Список актёров")
async def get_actors(db: DBDep) -> list[SActorGet]:
    return await ActorService(db).get_actors()


@router.get("/{actor_id}", summary="Получить актёра")
async def get_actor(actor_id: int, db: DBDep) -> SActorGet:
    try:
        return await ActorService(db).get_actor(actor_id)
    except ActorNotFoundError:
        raise ActorNotFoundHTTPError


@router.post("/", summary="Создать актёра")
async def create_actor(
    actor_data: SActorAdd,
    db: DBDep,
    is_admin: IsAdminDep,
):
    try:
        await ActorService(db).create_actor(actor_data)
    except ActorAlreadyExistsError:
        raise ActorAlreadyExistsHTTPError
    return {"status": "OK"}


@router.put("/{actor_id}", summary="Редактировать актёра")
async def edit_actor(
    actor_id: int,
    actor_data: SActorAdd,
    db: DBDep,
    is_admin: IsAdminDep,
):
    try:
        await ActorService(db).edit_actor(actor_id, actor_data)
    except ActorNotFoundError:
        raise ActorNotFoundHTTPError
    return {"status": "OK"}


@router.delete("/{actor_id}", summary="Удалить актёра")
async def delete_actor(
    actor_id: int,
    db: DBDep,
    is_admin: IsAdminDep,
):
    try:
        await ActorService(db).delete_actor(actor_id)
    except ActorNotFoundError:
        raise ActorNotFoundHTTPError
    return {"status": "OK"}