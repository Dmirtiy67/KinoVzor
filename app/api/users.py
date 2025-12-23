from fastapi import APIRouter

from app.api.dependencies import DBDep, IsAdminDep
from app.services.users import UserService
from app.schemes.users import SUserGet

router = APIRouter(prefix="/users", tags=["Пользователи"])


@router.get("/")
async def get_users(db: DBDep, is_admin: IsAdminDep) -> list[SUserGet]:
    return await UserService(db).get_users()


@router.delete("/{user_id}")
async def delete_user(
    user_id: int,
    db: DBDep,
    is_admin: IsAdminDep,
):
    await UserService(db).delete_user(user_id)
    return {"status": "OK"}