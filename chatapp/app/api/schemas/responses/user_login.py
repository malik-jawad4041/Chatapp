from pydantic import BaseModel


class LoginToken(BaseModel):
    """Pydantic model representing a login response token.

    Attributes:
        token (str): JWT token string returned after successful login.
    """

    token: str
