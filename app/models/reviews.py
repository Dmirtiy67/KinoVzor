from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.films import FilmModel
    from app.models.users import UserModel


class ReviewModel(Base):
    tablename = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    film_id: Mapped[int] = mapped_column(
    ForeignKey("films.id", ondelete="CASCADE"), nullable=False)
    user_id: Mapped[int] = mapped_column(
    ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    films: Mapped["FilmModel"] = relationship(back_populates="reviews")
    users: Mapped["UserModel"] = relationship(back_populates="reviews")
