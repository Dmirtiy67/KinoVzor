from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models.favourites import FavouriteModel
from app.repositories.base import BaseRepository
from app.schemes.favourites import SFavouriteGet
from app.schemes.relations_favourites import SFavouriteGetWithRels


class FavouritesRepository(BaseRepository):
    model = FavouriteModel
    schema = SFavouriteGet

    async def get_one_or_none_with_relations(self, **filter_by):
        query = (
            select(self.model)
            .filter_by(**filter_by)
            .options(
                selectinload(self.model.users),
                selectinload(self.model.films),
            )
        )

        result = await self.session.execute(query)

        model = result.scalars().one_or_none()
        if model is None:
            return None

        result = SFavouriteGetWithRels.model_validate(model, from_attributes=True)
        return result
