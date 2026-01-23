"""Interface for WebSocket services.

Defines the contract for handling JWT authentication, message sending,
and managing WebSocket connections.
"""

from abc import ABC, abstractmethod
from typing import Any
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession


class IWSService(ABC):
    """Abstract base class for WebSocket services."""

    @staticmethod
    @abstractmethod
    async def jwt_verify_and_append_list(
        session: AsyncSession,
        token: str,
        secret_key: str,
        algorithm: str,
        websocket: Any,
    ) -> str:
        """Verify JWT token and append the user to the active connection list.

        Args:
            session (AsyncSession): SQLAlchemy async session for database operations.
            token (str): JWT token provided by the user.
            secret_key (str): Secret key used for JWT decoding.
            algorithm (str): Algorithm used for JWT decoding.
            websocket (Any): WebSocket connection object for the user.
            redis (Any) : Redis connection object for the user.

        Returns:
            str: User ID extracted from the token.

        Raises:
            Exception: If JWT verification fails or user cannot be appended.
        """
        ...

    @staticmethod
    @abstractmethod
    async def send_message(
        session: AsyncSession,
        uid: str,
        message: str,
        redis: Redis,
    ):
        """Send a message to all connected clients in the user's room.

        Args:
            session (AsyncSession): SQLAlchemy async session for database operations.
            uid (str): User ID of the sender.
            redis (Redis): Redis connection object for the user.
            message (str): Message content to send.

        Raises:
            Exception: If sending the message fails.
        """
        ...

    @staticmethod
    @abstractmethod
    async def remove_from_list(uid: str, redis: Redis):
        """Remove a WebSocket connection from the active connection list.

        Args:
            uid (str): User ID of the sender.
            redis (Redis): Redis connection object for the user."""
        ...
