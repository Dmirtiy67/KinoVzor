from app.database.database import async_session_maker
from app.repositories.roles import RolesRepository
from app.repositories.users import UsersRepository
from app.repositories.films import FilmsRepository
from app.repositories.actors import ActorsRepository
from app.repositories.actors_in_films import ActorsInFilmsRepository
from app.repositories.reviews import ReviewsRepository
from app.repositories.favourites import FavouritesRepository


class DBManager:
    def __init__(self, session_factory: async_session_maker):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.users = UsersRepository(self.session)
        self.roles = RolesRepository(self.session)
        self.films = FilmsRepository(self.session)
        self.actors = ActorsRepository(self.session)
        self.actors_in_films = ActorsInFilmsRepository(self.session)
        self.reviews = ReviewsRepository(self.session)
        self.favourites = FavouritesRepository(self.session)

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()
