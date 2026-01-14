from functools import lru_cache
from chatapp.app.core.settings.base import JwtSettings, DBSettings


@lru_cache
def get_jwt_settings() -> JwtSettings:
    return JwtSettings()

@lru_cache
def get_postgres_settings() -> DBSettings :
    return DBSettings()