"""Utility functions to retrieve cached application settings.

Provides functions to get JWT and database settings using caching
to avoid redundant instantiation.
"""

from functools import lru_cache

from chatapp.app.core.settings.base import DBSettings, JwtSettings


@lru_cache
def get_jwt_settings() -> JwtSettings:
    """Get cached JWT settings.

    Returns:
        JwtSettings: Instance of JwtSettings containing JWT configuration.
    """
    return JwtSettings()


@lru_cache
def get_postgres_settings() -> DBSettings:
    """Get cached PostgreSQL database settings.

    Returns:
        DBSettings: Instance of DBSettings containing database configuration.
    """
    return DBSettings()
