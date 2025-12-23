from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
   from app.models.actors_in_films import ActorInFilmModel
   from app.models.favourites import FavouriteModel
   from app.models.reviews import ReviewModel


class FilmModel(Base):
   __tablename__ = "films"

   id: Mapped[int] = mapped_column(primary_key=True)
   name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
   image_url: Mapped[str] = mapped_column(String(500), nullable=True)
   description: Mapped[str] = mapped_column(String(2000), nullable=True)
   video_url: Mapped[str] = mapped_column(String(500), nullable=True)

   actors_in_films: Mapped[list["ActorInFilmModel"]] = relationship(back_populates="film", cascade="all, delete")
   favourites: Mapped[list["FavouriteModel"]] = relationship(back_populates="film", cascade="all, delete")
   reviews: Mapped[list["ReviewModel"]] = relationship(back_populates="film", cascade="all, delete")