from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FilmCreate(BaseModel):
    title: str
    description: Optional[str] = None
    director: Optional[str] = None

class FilmRead(FilmCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True