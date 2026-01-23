"""Dependency injection container for application services.

Provides a centralized way to configure and access services such as
authentication, user login, and WebSocket handling, along with
database session management.
"""
from collections.abc import AsyncIterator
from typing import Union
from redis import Redis
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)
from chatapp.app.core.config import (DBSettings, JwtSettings, get_jwt_settings,get_api_key,APISettings,
                                     get_postgres_settings)
from chatapp.app.domain.services.auth import IAuthService
from chatapp.app.domain.services.user_login import ILoginService
from chatapp.app.domain.services.websocket_connection import IWSService
from chatapp.app.services.auth import AuthService
from chatapp.app.services.user_login import LoginService
from chatapp.app.services.websocket_connection import WSService
from chatapp.app.infrastructure.repositories.websocket_connection import WebSocketEndpoint
from chatapp.app.domain.repositories.websocket_connection import IWebSocketEndpoint

import socketio

class Container:
    """Container for application services and database sessions."""

    def __init__(self, jwt: JwtSettings, db: DBSettings,key : APISettings) -> None:
        """Initialize the container with JWT and database settings.

        Args:
            jwt (JwtSettings): JWT configuration.
            db (DBSettings): Database configuration.
        """
        self.sio = socketio.AsyncServer
        self.redis: Union[Redis, None] = None
        self.key = key
        self.jwt = jwt
        self.db = db
        self._engine = create_async_engine(**db.sqlalchemy_engine_props)
        self._session = async_sessionmaker(bind=self._engine, expire_on_commit=False)

    async def session(self) -> AsyncIterator[AsyncSession]:
        """Provide an asynchronous database session.

        Yields:
            AsyncSession: An active SQLAlchemy asynchronous session.
        """
        async with self._session() as session:
            yield session
            await session.commit()

    @staticmethod
    def user_login() -> ILoginService:
        """Return the user login service instance.

        Returns:
            ILoginService: Implementation of the user login service.
        """
        return LoginService()

    @staticmethod
    def auth() -> IAuthService:
        """Return the authentication service instance.

        Returns:
            IAuthService: Implementation of the authentication service.
        """
        return AuthService()

    @staticmethod
    def I_websocket() -> IWebSocketEndpoint:
        """Return the web sockcet instance.

        Returns:
            IWebSocketEndpoint: Implementation of the WebSocket repository.
        """
        return WebSocketEndpoint()

    @staticmethod
    def websocket_conn() -> IWSService:
        """Return the WebSocket service instance.

        Returns:
            IWSService: Implementation of the WebSocket service.
        """
        return WSService()


container = Container(get_jwt_settings(), get_postgres_settings(), get_api_key())
"""Singleton container instance with cached JWT and DB settings."""
