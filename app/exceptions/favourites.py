from fastapi import HTTPException
from app.exceptions.base import ObjectAlreadyExistsError, ObjectNotFoundError

class FavouriteNotFoundError(ObjectNotFoundError):
    pass

class FavouriteAlreadyExistsError(ObjectAlreadyExistsError):
    pass

class FavouriteNotFoundHTTPError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Избранное не найдено")

class FavouriteAlreadyExistsHTTPError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Избранное уже существует")