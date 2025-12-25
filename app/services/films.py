from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database.database import Base
from app.schemas.films import FilmCreate

from sqlalchemy import Column, Integer, String, DateTime, func

class Film(Base):
    tablename = "films"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    director = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

async def create_film(db: AsyncSession, film: FilmCreate):
    new_film = Film(title=film.title, description=film.description, director=film.director)
    db.add(new_film)
    await db.commit()
    await db.refresh(new_film)
    return new_film

async def get_films(db: AsyncSession):
    result = await db.execute(select(Film))
    return result.scalars().all()