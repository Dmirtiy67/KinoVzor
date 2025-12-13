from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
   from app.models.actors_in_films import ActorInFilmModel
   

class ActorModel(Base):
   __tablename__ = "actors"

   id: Mapped[int] = mapped_column(primary_key=True)
   name: Mapped[str] = mapped_column(String(255), nullable=False)
   date: Mapped[date] = mapped_column(Date, nullable=False)
   description: Mapped[str] = mapped_column(String(2000), nullable=True)
   image_url: Mapped[str] = mapped_column(String(500), nullable=True)

   actors_in_films: Mapped[list["ActorInFilmModel"]] = relationship(back_populates="actor")

