from fastapi import APIRouter

from chatapp.app.api.routes.user_login import router
from chatapp.app.api.routes.websocket_connection import wsrouter
from chatapp.app.api.routes.centrifugo import ct_router
routes = APIRouter()

routes.include_router(router=router)
routes.include_router(router=wsrouter)
routes.include_router(router=ct_router)