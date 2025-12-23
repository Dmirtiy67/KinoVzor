from fastapi import APIRouter

from app.api.dependencies import DBDep, IsAdminDep
from app.schemes.reviews import SReviewAdd, SReviewGet
from app.services.reviews import ReviewService
from app.exceptions.reviews import ReviewNotFoundError, ReviewNotFoundHTTPError

router = APIRouter(prefix="/reviews", tags=["Отзывы"])


@router.get("/film/{film_id}")
async def get_reviews(film_id: int, db: DBDep) -> list[SReviewGet]:
    return await ReviewService(db).get_reviews_by_film(film_id)


@router.post("/")
async def create_review(review_data: SReviewAdd, db: DBDep):
    await ReviewService(db).create_review(review_data)
    return {"status": "OK"}


@router.delete("/{review_id}")
async def delete_review(
    review_id: int,
    db: DBDep,
    is_admin: IsAdminDep,
):
    try:
        await ReviewService(db).delete_review(review_id)
    except ReviewNotFoundError:
        raise ReviewNotFoundHTTPError
    return {"status": "OK"}
