from contextlib import asynccontextmanager
import socketio
from fastapi import FastAPI
from redis.asyncio import Redis

from chatapp.app.api.router import routes
from chatapp.app.core.container import container


@asynccontextmanager
async def lifespan(application: FastAPI):
    container.redis = Redis(host="127.0.0.1", port=6379, decode_responses=True)
    yield
    await container.redis.close()
    await container.redis.connection_pool.disconnect()


def create_app() -> FastAPI:

    application = FastAPI(lifespan=lifespan)
    application.include_router(router=routes)

    mgr = socketio.AsyncRedisManager("url")

    container.sio = socketio.AsyncServer(async_mode="asgi",client_manager=mgr)

    socket_app = socketio.ASGIApp(container.sio)  # Socket.IO as ASGI app

    application.mount("/ws", socket_app)

    return application


app = create_app()

# TEST THIS ENDPOINT
