"""Interface for authentication service.

Defines the contract for generating and verifying JWT tokens
used for user authentication.
"""

from abc import ABC, abstractmethod

from .....chatapp.app.domain.dtos.auth import PayloadDTO
from .....chatapp.app.domain.dtos.user_login import LoginDTO


class IAuthService(ABC):
    """Abstract base class for authentication services."""

    @staticmethod
    @abstractmethod
    def generate_token(
        body: LoginDTO, uid: str, secret_key: str, algorithm: str
    ) -> str:
        """Generate a JWT token for a given user.

        Args:
            body (LoginDTO): User login data transfer object.
            uid (str): Unique identifier of the user.
            secret_key (str): Secret key used for token encoding.
            algorithm (str): Algorithm used for token encoding.

        Returns:
            str: Encoded JWT token as a string.
        """

    @staticmethod
    @abstractmethod
    def verify_token(token: str, secret_key: str, algorithm: str) -> PayloadDTO:
        """Verify a JWT token and return the payload.

        Args:
            token (str): JWT token to verify.
            secret_key (str): Secret key used for token decoding.
            algorithm (str): Algorithm used for token decoding.

        Returns:
            PayloadDTO: Data transfer object containing the decoded payload.

        Raises:
            Exception: If token is invalid or expired.
        """