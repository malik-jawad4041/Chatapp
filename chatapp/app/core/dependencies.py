from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from chatapp.app.core.config import get_jwt_settings
from chatapp.app.core.settings.base import JwtSettings
from chatapp.app.services.user_login import LoginService

from ..services.auth import AuthService
from ..services.websocket_connection import WSService
from .container import container

DBSession = Annotated[AsyncSession, Depends(container.session)]
userLogin = Annotated[LoginService, Depends(container.user_login)]
jwt = Annotated[JwtSettings, Depends(get_jwt_settings)]
Auth = Annotated[AuthService, Depends(container.auth)]
WS = Annotated[WSService, Depends(container.websocket_conn)]
