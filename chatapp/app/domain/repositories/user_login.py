import uuid
from abc import ABC, abstractmethod
from ..dtos.user_login import LoginDTO
from  ..dtos.Users import UsersDTO
from typing import Union
from sqlalchemy.ext.asyncio import AsyncSession

class IUserLoginRepository(ABC):
    """USER_LOGIN repository interface."""

    @staticmethod
    @abstractmethod
    async def check_user_from_db(session : AsyncSession , body : LoginDTO) -> Union[UsersDTO,None] :...


    @staticmethod
    @abstractmethod
    async def add_user_to_db(session:AsyncSession,body: LoginDTO, uid:str) -> None:...

