from fastapi import HTTPException
from app.exceptions.base import ObjectAlreadyExistsError, ObjectNotFoundError

class UserNotFoundError(ObjectNotFoundError):
    """Пользователь не найден"""
    pass

class UserAlreadyExistsError(ObjectAlreadyExistsError):
    """Пользователь уже существует"""
    pass

class UserNotFoundHTTPError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Пользователь не найден")

class UserAlreadyExistsHTTPError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Пользователь уже существует")