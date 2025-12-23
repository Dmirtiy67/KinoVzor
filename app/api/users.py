from fastapi import APIRouter
from app.api.dependencies import DBDep, IsAdminDep
from app.schemes.users import SUserAdd, SUserGet
from app.services.auth import AuthService
from app.exceptions.users import (
    UserNotFoundHTTPError,
    UserAlreadyExistsHTTPError
)

router = APIRouter(prefix="/users", tags=["Пользователи"])


@router.post("/", summary="Регистрация нового пользователя")
async def create_user(user_data: SUserAdd, db: DBDep):
    try:
        await AuthService(db).register_user(user_data)
    except UserAlreadyExistsHTTPError:
        raise UserAlreadyExistsHTTPError()
    return {"status": "OK"}


@router.get("/{user_id}", summary="Получение данных пользователя")
async def get_user(user_id: int, db: DBDep):
    user = await AuthService(db).get_me(user_id=user_id)
    if not user:
        raise UserNotFoundHTTPError()
    return user
