"""API routes for user login operations.

Defines endpoints for logging in users and generating JWT tokens.
"""

from fastapi import APIRouter

from .....chatapp.app.api.schemas.requests.user_login import Login
from .....chatapp.app.api.schemas.responses.user_login import LoginToken
from .....chatapp.app.core.dependencies import DBSession, jwt, userLogin

router = APIRouter()


@router.post("/login", response_model=LoginToken)
async def login(
    body: Login,
    session: DBSession,
    service: userLogin,
    jwt_token: jwt,
):
    """Authenticate a user and return a JWT token.

    Checks if the user exists in the database. If not, a new user is added.
    Generates a JWT token for the user.

    Args:
        body (Login): User login data (username and password).
        session (DBSession): Database session dependency.
        service (userLogin): Login service dependency.
        jwt_token (jwt): JWT configuration dependency.

    Returns:
        LoginToken: Object containing the JWT token string.
    """
    token = await service.check_and_add_new_user(
        session, body, jwt_token.secret_key, jwt_token.algorithm
    )
    return LoginToken(token=str(token))
