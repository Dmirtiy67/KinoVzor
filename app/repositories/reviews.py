from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models.reviews import ReviewModel
from app.repositories.base import BaseRepository
from app.schemes.reviews import SReviewGet
from app.schemes.relations_reviews import SReviewGetWithRels


class ReviewsRepository(BaseRepository):
    model = ReviewModel
    schema = SReviewGet

    async def get_one_or_none_with_relations(self, **filter_by):
        query = (
            select(self.model)
            .filter_by(**filter_by)
            .options(
                selectinload(self.model.films),
                selectinload(self.model.users),
            )
        )

        result = await self.session.execute(query)

        model = result.scalars().one_or_none()
        if model is None:
            return None

        result = SReviewGetWithRels.model_validate(model, from_attributes=True)
        return result

