from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
   from app.models.films import FilmModel
   from app.models.actors import ActorModel


class ActorInFilmModel(Base):
    __tablename__ = "actors_in_films"

    id: Mapped[int] = mapped_column(primary_key=True)
    film_id: Mapped[int] = mapped_column(ForeignKey("films.id", ondelete="CASCADE"), nullable=False)
    actor_id: Mapped[int] = mapped_column(ForeignKey("actor.id", ondelete="CASCADE"), nullable=False)

    films: Mapped["FilmModel"] = relationship(back_populates="actors_in_films")
    actors: Mapped["ActorModel"] = relationship(back_populates="actors_in_films")
