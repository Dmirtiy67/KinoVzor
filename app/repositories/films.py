from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models.films import FilmModel
from app.repositories.base import BaseRepository
from app.schemes.films import SFilmGet
from app.schemes.relations_films import SFilmGetWithRels


class FilmsRepository(BaseRepository):
    model = FilmModel
    schema = SFilmGet

    async def get_one_or_none_with_relations(self, **filter_by):
        query = (
            select(self.model)
            .filter_by(**filter_by)
            .options(
                selectinload(self.model.actors_in_films),
                selectinload(self.model.favourites),
                selectinload(self.model.reviews),
            )
        )

        result = await self.session.execute(query)

        model = result.scalars().one_or_none()
        if model is None:
            return None

        result = SFilmGetWithRels.model_validate(model, from_attributes=True)
        return result
