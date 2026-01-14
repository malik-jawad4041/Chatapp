from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from chatapp.app.domain.dtos.Users import UsersDTO
from chatapp.app.domain.repositories.websocket_connection import IWebSocketEndpoint
from chatapp.app.infrastructure import db_modals
from sqlalchemy import select
from chatapp.app.infrastructure.mappers.user_login import Login
from chatapp.app.infrastructure.mappers.websocket_connection import WSMapper
from chatapp.app.domain.dtos.Chatroom import ChatRoomDTO


class WebSocketEndpoint(IWebSocketEndpoint):

    @staticmethod
    async def fetch_roomid(session : AsyncSession, uid:str) ->UsersDTO:

        stmt = select(db_modals.Users).where(db_modals.Users.id == uid)
        result = await session.execute(stmt)
        user = result.scalar()
        return Login.to_dto(user)


    @staticmethod
    async def add_message(session: AsyncSession, uid : str , message:str , receiver : str):

        room = ChatRoomDTO(
            id = uid,
            time = datetime.now(),
            message = message,
            receiver= receiver,
        )

        model = WSMapper.from_dto(room)
        session.add(model)
        await session.commit()





