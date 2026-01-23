"""Service for user login and registration in chatapp.

Provides functionality to check if a user exists, register new users,
and generate JWT tokens for authentication.
"""

import hashlib
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from chatapp.app.domain.dtos.user_login import LoginDTO
from chatapp.app.domain.dtos.Users import UsersDTO
from chatapp.app.domain.services.user_login import ILoginService
from chatapp.app.infrastructure.repositories.user_login import UserLoginRepository
from chatapp.app.services.auth import AuthService


class LoginService(ILoginService):
    """Concrete implementation of the login service interface.

    Handles user authentication and registration operations.
    """

    @staticmethod
    async def check_and_add_new_user(
        session: AsyncSession, body: LoginDTO, secret_key: str, algorithm: str
    ) -> str:
        """Checks if a user exists in the database, adds new user if not, and returns JWT.

        Args:
            session (AsyncSession): SQLAlchemy async session for DB operations.
            body (LoginDTO): User login data including username and password.
            secret_key (str): Secret key used to sign the JWT token.
            algorithm (str): JWT signing algorithm (e.g., 'HS256').

        Returns:
            str: JWT token for the authenticated or newly registered user.
        """
        user_in_db = await UserLoginRepository.check_user_from_db(session, body)

        if not user_in_db:  # if user_in_db is none
            uid = str(uuid.uuid4())
            password = hashlib.sha256(body.password.encode())
            body.password = password.hexdigest()
            await UserLoginRepository.add_user_to_db(session, body, uid)
            token = AuthService.generate_token(body, uid, secret_key, algorithm)
            return token
        else:
            token = AuthService.generate_token(
                body, str(user_in_db.id), secret_key, algorithm
            )
            return token
