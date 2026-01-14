from abc import ABC,abstractmethod
from chatapp.app.domain.dtos.user_login import LoginDTO
from chatapp.app.domain.dtos.auth import PayloadDTO



class IAuthService(ABC):

    @staticmethod
    @abstractmethod
    def generate_token(body : LoginDTO , uid : str ,secret_key:str,algorithm:str)->str:...

    @staticmethod
    @abstractmethod
    def verify_token(token : str,secret_key : str, algorithm : str)->PayloadDTO :...

