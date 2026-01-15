"""WebSocket endpoint for real-time communication.

Handles client connections, JWT authentication, and message passing
via WebSockets.
"""

import uuid
from typing import Annotated

from fastapi import APIRouter, Header, WebSocket, WebSocketDisconnect
from chatapp.app.core.dependencies import  redis , WS,DBSession,jwt
wsrouter = APIRouter()


@wsrouter.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    authorization: Annotated[str, Header()],
    jwt_token: jwt,
    session: DBSession,
):
    """WebSocket endpoint to authenticate and communicate with clients.

    Verifies the JWT token, appends the client to the active connections list,
    and handles incoming messages. Messages are stored in the database and
    sent to users in the same room. Removes the client from the connection list
    on disconnect.

    Args:
        websocket (WebSocket): WebSocket connection instance.
        authorization (str, Header): JWT token passed in the Authorization header.
        jwt_token (jwt): JWT configuration dependency.
        session (DBSession): Database session dependency.
    """

    uid = await WS.jwt_verify_and_append_list(
        session, authorization, jwt_token.secret_key, jwt_token.algorithm, websocket,redis
    )
    raw_data = uuid.uuid4()
    print(raw_data)
    await websocket.accept()
    await websocket.send_json({"id": uid})

    try:
        while True:
            data = await websocket.receive_text()  # It expects a message field
            await WS.send_message(session, uid, data,redis)

    except WebSocketDisconnect:
        WS.remove_from_list(uid,redis)

