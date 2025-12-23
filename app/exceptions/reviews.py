from fastapi import HTTPException
from app.exceptions.base import ObjectAlreadyExistsError, ObjectNotFoundError

class ReviewNotFoundError(ObjectNotFoundError):
    pass

class ReviewAlreadyExistsError(ObjectAlreadyExistsError):
    pass

class ReviewNotFoundHTTPError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Отзыв не найден")

class ReviewAlreadyExistsHTTPError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Отзыв уже существует")