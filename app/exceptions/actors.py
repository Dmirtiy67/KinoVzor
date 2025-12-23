from fastapi import HTTPException
from app.exceptions.base import ObjectAlreadyExistsError, ObjectNotFoundError

class FilmNotFoundError(ObjectNotFoundError):
    pass

class FilmAlreadyExistsError(ObjectAlreadyExistsError):
    pass

class FilmNotFoundHTTPError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Фильм не найден")

class FilmAlreadyExistsHTTPError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Фильм уже существует")