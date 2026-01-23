"""Utility functions to retrieve cached application settings.

Provides functions to get JWT and database settings using caching
to avoid redundant instantiation.
"""

from functools import lru_cache

from chatapp.app.core.settings.base import DBSettings, JwtSettings , APISettings



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


@lru_cache
def get_api_key() -> APISettings:
    """Get cached api key settings.

        Returns:
            APISettings: Instance of APISettings containing api key.
        """
    return APISettings()
