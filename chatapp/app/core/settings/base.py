from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class JwtSettings(BaseSettings):
    secret_key: str
    algorithm: str

    model_config = SettingsConfigDict(env_file=".env.jwt")

class APISettings(BaseSettings):
    secret_key: str
    model_config = SettingsConfigDict(env_file=".env.key", case_sensitive=False)


class DBSettings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int
    postgres_db: str

    @computed_field  # type: ignore
    @property
    def sql_db_uri(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_host,
            port=self.postgres_port,
            database=self.postgres_db,
        )

    @computed_field  # type: ignore
    @property
    def sqlalchemy_engine_props(self) -> dict:
        return dict(url=self.sql_db_uri)

    model_config = SettingsConfigDict(env_file=".env.db")
