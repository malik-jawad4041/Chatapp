from chatapp.app.domain.dtos.user_login import LoginDTO
from chatapp.app.domain.services.auth import IAuthService
import jwt
from datetime import datetime, timedelta
from chatapp.app.core.exceptions import WebsocketUnauthorized
from chatapp.app.domain.dtos.auth import PayloadDTO


class AuthService(IAuthService):

    @staticmethod
    def generate_token(body: LoginDTO,uid:str,secret_key:str,algorithm:str)->str:
        payload = {
            "id": uid,
            "username": body.username,
            "exp": datetime.now() + timedelta(minutes=30)  # token expires in 30 mins
        }
        token = jwt.encode(payload, secret_key, algorithm=algorithm)
        return token

    @staticmethod
    def verify_token(token:str,secret_key:str,algorithm:str)->PayloadDTO:
        try:
            payload = jwt.decode(token, secret_key, algorithms=algorithm)
            return PayloadDTO(
                id = payload["id"],
                username = payload["username"],
            )

        except Exception as e:
            raise WebsocketUnauthorized()