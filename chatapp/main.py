from fastapi import FastAPI

from chatapp.app.api.router import routes


def create_app() -> FastAPI:
    application = FastAPI()
    application.include_router(router=routes)

    return application


app = create_app()


# TEST THIS ENDPOINT
