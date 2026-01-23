from typing import Annotated

from fastapi import Depends, APIRouter
from redis import Redis
import socketio

from chatapp.app.services.auth import AuthService
from chatapp.app.services.websocket_connection import WSService
from sqlalchemy.ext.asyncio import AsyncSession

from chatapp.app.core.config import get_jwt_settings , get_api_key
from chatapp.app.core.settings.base import JwtSettings,APISettings
from chatapp.app.services.user_login import LoginService
from .container import container
from chatapp.app.infrastructure.repositories.websocket_connection import WebSocketEndpoint



DBSession = Annotated[AsyncSession, Depends(container.session)]
userLogin = Annotated[LoginService, Depends(container.user_login)]
jwt = Annotated[JwtSettings, Depends(get_jwt_settings)]
key = Annotated[APISettings,Depends(get_api_key)]
Auth = Annotated[AuthService, Depends(container.auth)]
WS = Annotated[WSService, Depends(container.websocket_conn)]
redis = Annotated[Redis, Depends(container.redis)]
sio = Annotated[socketio.AsyncServer,Depends(container.sio)]
IWS = Annotated[WebSocketEndpoint, Depends(container.I_websocket)]
