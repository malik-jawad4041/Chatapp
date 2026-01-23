"""Authentication service implementation for chatapp.

Provides methods to generate and verify JWT tokens for user authentication.
"""

from datetime import datetime, timedelta

import jwt

from chatapp.app.core.exceptions import WebsocketUnauthorized
from chatapp.app.domain.dtos.auth import PayloadDTO
from chatapp.app.domain.dtos.user_login import LoginDTO
from chatapp.app.domain.services.auth import IAuthService


class AuthService(IAuthService):
    """Concrete implementation of the authentication service interface.

    Provides functionality to generate JWT tokens and verify them.
    """

    @staticmethod
    def generate_token(
        body: LoginDTO, uid: str, secret_key: str, algorithm: str
    ) -> str:
        """Generates a JWT token for a given user.

        Args:
            body (LoginDTO): The login data transfer object containing username.
            uid (str): The unique user identifier.
            secret_key (str): The secret key used to sign the token.
            algorithm (str): The JWT algorithm to use (e.g., 'HS256').

        Returns:
            str: The encoded JWT token with a 30-minute expiration.
        """
        payload = {
            "sub": uid,
            "username": body.username,
            "exp": datetime.now() + timedelta(minutes=60),  # token expires in 30 mins
        }
        token = jwt.encode(payload, secret_key, algorithm=algorithm)
        return token

    @staticmethod
    def verify_token(token: str, secret_key: str, algorithm: str) -> PayloadDTO:
        """Verifies a JWT token and returns the payload.

        Args:
            token (str): The JWT token to verify.
            secret_key (str): The secret key used to decode the token.
            algorithm (str): The JWT algorithm to use for decoding.

        Returns:
            PayloadDTO: Data transfer object containing user id and username.

        Raises:
            WebsocketUnauthorized: If token verification fails or token is invalid.
        """
        try:
            payload = jwt.decode(token, secret_key, algorithms=algorithm)
            return PayloadDTO(
                id=payload["id"],
                username=payload["username"],
            )
        except Exception as e:
            raise WebsocketUnauthorized()
