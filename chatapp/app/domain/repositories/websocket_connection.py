from abc import ABC, abstractmethod
from chatapp.app.domain.dtos.Users import UsersDTO
from sqlalchemy.ext.asyncio import AsyncSession


class IWebSocketEndpoint(ABC):
    """USER_LOGIN repository interface."""

    @staticmethod
    @abstractmethod
    async def fetch_roomid(session : AsyncSession, uid:str)->UsersDTO:...


    @staticmethod
    @abstractmethod
    async def add_message(session: AsyncSession, uid : str , message:str , receiver : str):...



