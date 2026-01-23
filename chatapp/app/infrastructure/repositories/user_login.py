"""Repository for user login operations.

Provides methods to check if a user exists in the database
and to add a new user.
"""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from chatapp.app.domain.dtos.user_login import LoginDTO
from chatapp.app.domain.repositories.user_login import IUserLoginRepository
from chatapp.app.infrastructure.db_modals import Users

from chatapp.app.infrastructure import db_modals
from chatapp.app.infrastructure.mappers.user_login import Login


class UserLoginRepository(IUserLoginRepository):
    """Concrete implementation of the user login repository interface.

    Handles database interactions for user login and registration.
    """

    @staticmethod
    async def check_user_from_db(session: AsyncSession, body: LoginDTO):
        """Checks if a user exists in the database by username.

        Args:
            session (AsyncSession): SQLAlchemy async session for DB operations.
            body (LoginDTO): Data transfer object containing the username to check.

        Returns:
            LoginDTO | None: Returns a LoginDTO if the user exists, otherwise None.
        """
        stmt = select(db_modals.Users).where(db_modals.Users.username == body.username)
        result = await session.execute(stmt)
        user = result.scalars().first()
        if not user:
            return None
        return Login.to_dto(user)

    @staticmethod
    async def add_user_to_db(session: AsyncSession, body: LoginDTO, uid: str) -> None:
        """Adds a new user to the database.

        Args:
            session (AsyncSession): SQLAlchemy async session for DB operations.
            body (LoginDTO): Data transfer object containing username and password.
            uid (str): Unique identifier for the new user.

        Returns:
            None
        """
        user = Users(username=body.username, password=body.password, id=uid)
        session.add(user)
        await session.flush()
