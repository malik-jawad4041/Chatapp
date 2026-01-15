"""Interface for login service.

Defines the contract for checking users and generating authentication tokens.
"""

from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from .....chatapp.app.domain.dtos.user_login import LoginDTO


class ILoginService(ABC):
    """Abstract base class for login services."""

    @staticmethod
    @abstractmethod
    async def check_and_add_new_user(
        session: AsyncSession, body: LoginDTO, secret_key: str, algorithm: str
    ) -> str:
        """Check if a user exists and add them if not, returning a JWT token.

        Args:
            session (AsyncSession): SQLAlchemy async session for database operations.
            body (LoginDTO): User login data transfer object containing username and password.
            secret_key (str): Secret key used for JWT encoding.
            algorithm (str): Algorithm used for JWT encoding.

        Returns:
            str: JWT token for the user.

        Raises:
            Exception: If any database or authentication error occurs.
        """
        ...
