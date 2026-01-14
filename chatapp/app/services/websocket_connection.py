from sqlalchemy.ext.asyncio import AsyncSession
from chatapp.app.domain.services.websocket_connection import IWSService
from chatapp.app.services.auth import AuthService
from typing import Any
from chatapp.app.infrastructure.repositories.websocket_connection import WebSocketEndpoint


class WSService(IWSService):

    connection = []

    @staticmethod
    async def jwt_verify_and_append_list(session : AsyncSession,token:str,secret_key:str,algorithm:str,websocket : Any)->str:# id
        payload = AuthService.verify_token(token,secret_key,algorithm)
        uid = payload.id
        user = await WebSocketEndpoint.fetch_roomid(session, uid)
        client = {"id": uid, "clt": websocket, "room_id": user.roomid}
        WSService.connection.append(client)
        return payload.id


    @staticmethod
    async def send_message(session : AsyncSession,uid:str,message:str):
        # retrieve the room_id from db
        # add the message in the db
        # send message to user if it is online

        user = await WebSocketEndpoint.fetch_roomid(session, uid)
        await WebSocketEndpoint.add_message(session, uid , message,user.roomid)
        for i in WSService.connection:
                if i["room_id"] == user.roomid:
                    await i["clt"].send_json(message)


    @staticmethod
    async def remove_from_list(websocket:Any):
        for i in WSService.connection:
                if i["clt"] == websocket:
                    WSService.connection.remove(i)


