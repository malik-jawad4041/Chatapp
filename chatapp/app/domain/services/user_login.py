from abc import ABC,abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from chatapp.app.domain.dtos.user_login import LoginDTO


class ILoginService(ABC):

    @staticmethod
    @abstractmethod
    async def check_and_add_new_user(session:AsyncSession, body : LoginDTO ,secret_key:str , algorithm:str)->str:...

