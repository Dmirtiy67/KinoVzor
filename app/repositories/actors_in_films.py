from sqlalchemy import select
from app.models.actors_in_films import ActorInFilmModel
from app.repositories.base import BaseRepository
from app.schemes.actors_in_films import SActorInFilmGet


class ActorsInFilmsRepository(BaseRepository):
    model = ActorInFilmModel
    schema = SActorInFilmGet

    async def get_one_or_none_with_actor_and_film(self, **filter_by):
        query = (
            select(self.model)
            .filter_by(**filter_by)
            .options(
                
                selectinload(self.model.actors),
                selectinload(self.model.films),
            )
        )

        result = await self.session.execute(query)

        model = result.scalars().one_or_none()
        if model is None:
            return None

        
        return self.schema.model_validate(model, from_attributes=True)
