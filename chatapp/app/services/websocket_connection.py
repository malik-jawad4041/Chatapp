"""WebSocket service for chatapp.

Handles JWT verification, user connection tracking, message sending,
and connection removal for WebSocket clients.
"""

from typing import Any

from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from chatapp.app.domain.services.websocket_connection import IWSService
from chatapp.app.infrastructure.redis.wsendpoint import RepoRedis
from chatapp.app.infrastructure.repositories.websocket_connection import \
    WebSocketEndpoint

from chatapp.app.services.auth import AuthService


class WSService(IWSService):
    """Concrete implementation of WebSocket service interface.

    Maintains active WebSocket connections and provides methods to
    verify tokens, send messages, and remove connections.
    """

    @staticmethod
    async def jwt_verify_and_append_list(
        session: AsyncSession,
        token: str,
        secret_key: str,
        algorithm: str,
        websocket: Any,
    ) -> str:
        """Verifies a JWT token, fetches the user's room ID, and adds the client to the connection list.

        Args:
            session (AsyncSession): SQLAlchemy async session for DB operations.
            token (str): JWT token of the user.
            secret_key (str): Secret key used to decode the token.
            algorithm (str): JWT algorithm for decoding.
            websocket (Any): The WebSocket client instance.

        Returns:
            str: The verified user ID from the token payload.
        """
        payload = AuthService.verify_token(token, secret_key, algorithm)
        uid = payload.id
        user = await WebSocketEndpoint.fetch_roomid(session, uid)
        client = {"id": uid, "clt": websocket, "room_id": user.roomid}
        #await RepoRedis.store_data(client, redis)
        return payload.id

    @staticmethod
    async def send_message(session: AsyncSession, uid: str, message: str, redis: Redis):
        """Sends a message to all WebSocket clients in the same room and stores it in the database.

        Args:
            session (AsyncSession): SQLAlchemy async session for DB operations.
            uid (str): ID of the user sending the message.
            redis (Redis) : Redis connection object for the user.
            message (str): The message content to send.

        """
        # retrieve the room_id from db
        # add the message in the db
        # send message to user if it is online
        user = await WebSocketEndpoint.fetch_roomid(session, uid)
        await WebSocketEndpoint.add_message(session, uid, message, user.roomid)
        data = await RepoRedis.fetch_data(uid, redis)
        if data:
            await data["clt"].send_json(message)

    @staticmethod
    async def remove_from_list(uid: str, redis: Redis):
        """Removes a WebSocket client from the active connection list.

        Args:
            uid (str): ID of the user sending the message.
            redis (Redis) : Redis connection object for the user.
        """

        await RepoRedis.remove_data(uid, redis)
