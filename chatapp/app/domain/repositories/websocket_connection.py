from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from chatapp.app.domain.dtos.Users import UsersDTO


class IWebSocketEndpoint(ABC):
    """Interface for WebSocket data access operations.

    Defines the contract for operations related to WebSocket connections
    and messaging persistence.

    Methods:
        fetch_roomid(session, uid):
            Retrieves user information including the room ID.
        add_message(session, uid, message, receiver):
            Adds a message to the database for a specific user/room.
    """

    @staticmethod
    @abstractmethod
    async def fetch_roomid(session: AsyncSession, uid: str) -> UsersDTO:
        """Fetch user data including room ID from the database.

        Args:
            session (AsyncSession): SQLAlchemy async session object.
            uid (str): Unique identifier of the user.

        Returns:
            UsersDTO: Data transfer object containing user details.
        """
        ...

    @staticmethod
    @abstractmethod
    async def add_message(session: AsyncSession, uid: str, message: str, receiver: str):
        """Store a message in the database for a given user and receiver.

        Args:
            session (AsyncSession): SQLAlchemy async session object.
            uid (str): Unique identifier of the sender.
            message (str): Message content to store.
            receiver (str): Identifier of the message receiver.

        Returns:
            None
        """
        ...
