from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models.actors import ActorModel
from app.repositories.base import BaseRepository
from app.schemes.actors import SActorGet
from app.schemes.relations_actors_films import SActorGetWithRels


class ActorsRepository(BaseRepository):
    model = ActorModel
    schema = SActorGet

    async def get_one_or_none_with_films(self, **filter_by):
        query = (
            select(self.model)
            .filter_by(**filter_by)
            .options(selectinload(self.model.actors_in_films))
        )

        result = await self.session.execute(query)

        model = result.scalars().one_or_none()
        if model is None:
            return None

        result = SActorGetWithRels.model_validate(model, from_attributes=True)
        return result
