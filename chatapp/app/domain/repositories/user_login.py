import uuid
from abc import ABC, abstractmethod
from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession

from chatapp.app.domain.dtos.user_login import LoginDTO
from chatapp.app.domain.dtos.Users import UsersDTO


class IUserLoginRepository(ABC):
    """Interface for User Login Repository.

    This defines the contract for user login data access operations.

    Methods:
        check_user_from_db(session, body):
            Checks if a user exists in the database.
        add_user_to_db(session, body, uid):
            Adds a new user to the database.
    """

    @staticmethod
    @abstractmethod
    async def check_user_from_db(
        session: AsyncSession, body: LoginDTO
    ) -> Union[UsersDTO, None]:
        """Check if a user exists in the database.

        Args:
            session (AsyncSession): SQLAlchemy async session object.
            body (LoginDTO): Data transfer object containing username and password.

        Returns:
            Union[UsersDTO, None]: Returns a UsersDTO if found, otherwise None.
        """
        ...

    @staticmethod
    @abstractmethod
    async def add_user_to_db(session: AsyncSession, body: LoginDTO, uid: str) -> None:
        """Add a new user to the database.

        Args:
            session (AsyncSession): SQLAlchemy async session object.
            body (LoginDTO): Data transfer object containing username and password.
            uid (str): Unique identifier for the new user.

        Returns:
            None
        """
        ...
