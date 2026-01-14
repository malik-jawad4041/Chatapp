from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from collections.abc import AsyncIterator

from chatapp.app.services.user_login import LoginService
from chatapp.app.domain.services.user_login import ILoginService
from chatapp.app.core.config import JwtSettings, DBSettings
from chatapp.app.core.config import get_jwt_settings , get_postgres_settings
from chatapp.app.domain.services.auth import IAuthService
from chatapp.app.services.auth import AuthService
from chatapp.app.services.websocket_connection import WSService
from chatapp.app.domain.services.websocket_connection import IWSService



class Container:

    def __init__(self, jwt: JwtSettings,db : DBSettings ) -> None:
        self.jwt = jwt
        self.db = db
        self._engine = create_async_engine(**db.sqlalchemy_engine_props)
        self._session = async_sessionmaker(bind=self._engine, expire_on_commit=False)


    async def session(self) ->AsyncIterator[AsyncSession]:

        async with self._session() as session:
                yield session
                await session.commit()

    @staticmethod
    def user_login()-> ILoginService:
        return LoginService()

    @staticmethod
    def auth()->IAuthService:
        return AuthService()

    @staticmethod
    def websocket_conn()->IWSService:
        return WSService()


container = Container(get_jwt_settings(),get_postgres_settings())



