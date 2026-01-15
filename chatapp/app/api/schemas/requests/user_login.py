from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

from ......chatapp.app.domain.dtos import user_login

class Login(BaseModel):
    """Pydantic model representing user login credentials."""

    username: str
    password: str


class Settings(BaseSettings):
    """Application settings for JWT authentication.

    Attributes:
        secret_key (str): Secret key used for encoding/decoding JWT tokens.
        algorithm (str): Algorithm used for JWT token generation.
    """

    secret_key: str
    algorithm: str
    model_config = SettingsConfigDict(env_file=".env")


class LoginRequest(BaseModel):
    """Pydantic model for login request payload.

    Attributes:
        data (Login): Nested Login model containing username and password.
    """

    data: Login

    def to_dto(self) -> user_login.LoginDTO:
        """Convert the LoginRequest to a domain DTO (Data Transfer Object).

        Returns:
            LoginDTO: Domain object representing user login credentials.
        """
        return user_login.LoginDTO(
            username=self.data.username,
            password=self.data.password,
        )
