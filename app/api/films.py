from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.films import create_film, get_films
from app.schemas.films import FilmCreate, FilmRead
from app.database.database import async_session_maker

router = APIRouter()

async def get_db():
    async with async_session_maker() as session:
        yield session

@router.post("/", response_model=FilmRead)
async def create_new_film(film: FilmCreate, db: AsyncSession = Depends(get_db)):
    return await create_film(db, film)

@router.get("/", response_model=list[FilmRead])
async def read_films(db: AsyncSession = Depends(get_db)):
    return await get_films(db)