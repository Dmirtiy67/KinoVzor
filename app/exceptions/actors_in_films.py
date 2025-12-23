from fastapi import HTTPException
from app.exceptions.base import ObjectAlreadyExistsError, ObjectNotFoundError

class ActorInFilmNotFoundError(ObjectNotFoundError):
    pass

class ActorInFilmAlreadyExistsError(ObjectAlreadyExistsError):
    pass

class ActorInFilmNotFoundHTTPError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Связь актер/фильм не найдена")

class ActorInFilmAlreadyExistsHTTPError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Связь актер/фильм уже существует")