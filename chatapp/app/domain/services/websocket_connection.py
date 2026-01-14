from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any

class IWSService(ABC):

    @staticmethod
    @abstractmethod
    async def jwt_verify_and_append_list(session : AsyncSession,token:str,secret_key:str,algorithm:str ,websocket:Any)->str:...


    @staticmethod
    @abstractmethod
    async def send_message(session : AsyncSession,uid:str, message:str):...


    @staticmethod
    @abstractmethod
    async def remove_from_list(websocket:Any):...
