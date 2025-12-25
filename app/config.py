from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    DB_NAME: str
    DB_DRIVER: str = "sqlite+aiosqlite"

    @property
    def get_db_url(self) -> str:
        return f"{self.DB_DRIVER}:///{self.DB_NAME}.db"

    class Config:
        env_file = ".env"


settings = Settings()