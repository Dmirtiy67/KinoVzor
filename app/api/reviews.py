from fastapi import APIRouter
from app.api.dependencies import DBDep, IsAdminDep
from app.schemes.reviews import SReviewAdd, SReviewGet
from app.services.reviews import ReviewService
from app.exceptions.reviews import ReviewNotFoundHTTPError, ReviewAlreadyExistsHTTPError

router = APIRouter(prefix="/reviews", tags=["Отзывы"])


@router.post("/", summary="Добавление отзыва")
async def add_review(review_data: SReviewAdd, db: DBDep):
    try:
        await ReviewService(db).add_review(review_data)
    except ReviewAlreadyExistsHTTPError:
        raise ReviewAlreadyExistsHTTPError()
    return {"status": "OK"}


@router.get("/", summary="Список всех отзывов")
async def get_reviews(db: DBDep):
    return await ReviewService(db).get_all_reviews()


@router.get("/{review_id}", summary="Получение конкретного отзыва")
async def get_review(review_id: int, db: DBDep):
    review = await ReviewService(db).get_review(review_id)
    if not review:
        raise ReviewNotFoundHTTPError()
    return review

