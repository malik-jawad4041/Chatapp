from fastapi import APIRouter

from chatapp.app.api.routes.user_login import router
from chatapp.app.api.routes.websocket_connection import wsrouter

routes = APIRouter()

routes.include_router(router=router)
routes.include_router(router=wsrouter)
