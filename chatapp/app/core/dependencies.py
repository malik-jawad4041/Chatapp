from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from .container import container
from fastapi import Depends
from chatapp.app.services.user_login import LoginService
from chatapp.app.core.settings.base import JwtSettings
from chatapp.app.core.config import get_jwt_settings
from ..services.auth import AuthService
from ..services.websocket_connection import WSService



DBSession = Annotated[AsyncSession, Depends(container.session)]
userLogin = Annotated[LoginService, Depends(container.user_login)]
jwt = Annotated[JwtSettings,Depends(get_jwt_settings)]
Auth = Annotated[AuthService,Depends(container.auth)]
WS = Annotated[WSService,Depends(container.websocket_conn)]