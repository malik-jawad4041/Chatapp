from sqlalchemy.ext.asyncio import AsyncSession
from ..domain.dtos.user_login import LoginDTO
from ..domain.services.user_login import ILoginService
from ..infrastructure.repositories.user_login import UserLoginRepository
from ..domain.dtos.Users import UsersDTO
import hashlib
import uuid
from ..services.auth import AuthService


class LoginService(ILoginService):

    @staticmethod
    async def check_and_add_new_user(session:AsyncSession, body:LoginDTO,secret_key:str , algorithm:str) ->str: # return JWT

        user_in_db = await UserLoginRepository.check_user_from_db(session,body)

        if not user_in_db:  # if user_in_db is none
            uid  = str(uuid.uuid4())
            password = hashlib.sha256(body.password.encode())
            body.password = password.hexdigest()
            await UserLoginRepository.add_user_to_db(session,body,uid)
            token =  AuthService.generate_token(body, uid, secret_key, algorithm)
            return token
        else:
            token = AuthService.generate_token(body, str(user_in_db.id), secret_key, algorithm)
            return token



        
