"""Repository for WebSocket-related database operations.

Provides methods to fetch user room information and add messages
to the chatroom in the database.
"""

from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .....chatapp.app.domain.dtos.Chatroom import ChatRoomDTO
from .....chatapp.app.domain.dtos.Users import UsersDTO
from .....chatapp.app.domain.repositories.websocket_connection import \
    IWebSocketEndpoint
from .....chatapp.app.infrastructure import db_modals
from .....chatapp.app.infrastructure.mappers.user_login import Login
from .....chatapp.app.infrastructure.mappers.websocket_connection import WSMapper


class WebSocketEndpoint(IWebSocketEndpoint):
    """Concrete implementation of WebSocket repository interface.

    Handles database interactions related to WebSocket users and messages.
    """

    @staticmethod
    async def fetch_roomid(session: AsyncSession, uid: str) -> UsersDTO:
        """Fetches the user information for a given user ID.

        Args:
            session (AsyncSession): SQLAlchemy async session for DB operations.
            uid (str): The unique identifier of the user.

        Returns:
            UsersDTO: Data transfer object containing user information.
        """
        stmt = select(db_modals.Users).where(db_modals.Users.id == uid)
        result = await session.execute(stmt)
        user = result.scalar()
        return Login.to_dto(user)

    @staticmethod
    async def add_message(session: AsyncSession, uid: str, message: str, receiver: str):
        """Adds a message to the chatroom database.

        Args:
            session (AsyncSession): SQLAlchemy async session for DB operations.
            uid (str): The unique identifier of the sender.
            message (str): The message content.
            receiver (str): The receiver's room identifier.

        Returns:
            None
        """
        room = ChatRoomDTO(
            id=uid,
            time=datetime.now(),
            message=message,
            receiver=receiver,
        )

        model = WSMapper.from_dto(room)
        session.add(model)
        await session.commit()
