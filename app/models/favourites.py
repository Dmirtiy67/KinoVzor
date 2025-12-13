from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
   from app.models.users import UserModel
   from app.models.films import FilmModel
   
class FavouriteModel(Base):
   __tablename__ = "favourites"

   id: Mapped[int] = mapped_column(primary_key=True)
   user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
   film_id: Mapped[int] = mapped_column(ForeignKey("films.id", ondelete="CASCADE"), nullable=False)
   status: Mapped[str] = mapped_column(String(50), nullable=False)

   users: Mapped["UserModel"] = relationship(back_populates="favourites")
   films: Mapped["FilmModel"] = relationship(back_populates="favourites")