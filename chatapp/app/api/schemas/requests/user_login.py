from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict , BaseSettings
from chatapp.app.domain.dtos import user_login


class Login(BaseModel):
    username: str
    password: str


class Settings(BaseSettings):
    secret_key: str
    algorithm : str
    model_config = SettingsConfigDict(env_file=".env")


class LoginRequest(BaseModel):
    data : Login

    def to_dto(self):
        return user_login.LoginDTO(
            username = self.data.username,
            password = self.data.password,
        )
