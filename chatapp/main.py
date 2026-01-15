from fastapi import FastAPI
from contextlib import asynccontextmanager
from chatapp.app.api.router import routes
from chatapp.app.core.container import container
from redis.asyncio import Redis

@asynccontextmanager
async def lifespan(application: FastAPI):
    container.redis = Redis(host="127.0.0.1", port=6379, decode_responses=True)
    yield
    await container.redis.close()
    await container.redis.connection_pool.disconnect()


def create_app() -> FastAPI:
    application = FastAPI(lifespan=lifespan)
    application.include_router(router=routes)

    return application


app = create_app()

# TEST THIS ENDPOINT
