from fastapi import APIRouter, Depends
from app.services.auth import AuthService
from app.database.db_manager import DBDep
from app.schemes.users import SUserAdd
from app.schemes.roles import SRoleAdd

router = APIRouter(prefix="/admin", tags=["Админ"])

@router.post("/create_admin")
async def create_admin(db: DBDep):
    """
    Создаёт администратора с email admin@example.com и паролем admin123
    """
    # 1. Проверяем, есть ли роль admin
    admin_role = await db.roles.get_one_or_none(name="admin")
    if not admin_role:
        admin_role_data = SRoleAdd(name="admin")
        admin_role = await db.roles.add(admin_role_data)
        await db.commit()

    # 2. Проверяем, есть ли уже админ
    admin_user = await db.users.get_one_or_none(email="admin@example.com")
    if admin_user:
        return {"status": "Админ уже существует"}

    # 3. Создаём нового администратора
    hashed_password = AuthService.hash_password("admin123")
    admin_user_data = SUserAdd(
        name="Legasy",
        email="admin@example.com",
        hashed_password=hashed_password,
        role_id=admin_role.id
    )
    await db.users.add(admin_user_data)
    await db.commit()

    return {"status": "Админ создан!"}
