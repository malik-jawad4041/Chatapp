import uuid
from typing import Annotated

from fastapi import APIRouter, Header, WebSocket, WebSocketDisconnect

from chatapp.app.core.dependencies import WS, DBSession, jwt

wsrouter = APIRouter()


@wsrouter.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    authorization: Annotated[str, Header()],
    jwt_token: jwt,
    session: DBSession,
):
    uid = await WS.jwt_verify_and_append_list(
        session, authorization, jwt_token.secret_key, jwt_token.algorithm, websocket
    )
    raw_data = uuid.uuid4()
    print(raw_data)
    await websocket.accept()
    await websocket.send_json({"id": uid})

    try:
        while True:
            data = await websocket.receive_text()  # It expects a message field
            await WS.send_message(session, uid, data)

    except WebSocketDisconnect:
        WS.remove_from_list(websocket)
