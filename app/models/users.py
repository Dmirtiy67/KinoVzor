from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.roles import RoleModel
    from app.models.favourites import FavouriteModel
    from app.models.reviews import ReviewModel
    

class UserModel(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(200), nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)

    roles: Mapped["RoleModel"] = relationship(back_populates="users")
    favourites: Mapped[list["FavouriteModel"]] = relationship(back_populates="user", cascade="all, delete")
    reviews: Mapped[list["ReviewModel"]] = relationship(back_populates="user", cascade="all, delete")