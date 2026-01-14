from fastapi import APIRouter
from chatapp.app.api.schemas.requests.user_login import Login
from chatapp.app.core.dependencies import DBSession,userLogin, jwt
from chatapp.app.api.schemas.responses.user_login import LoginToken

router = APIRouter()

@router.post("/login",response_model=LoginToken) # ADD A RESPONSE MODEL
async def login(body : Login,
                session: DBSession,
                service: userLogin,
                jwt_token: jwt
                ):

    token = await service.check_and_add_new_user(session,body,jwt_token.secret_key,jwt_token.algorithm)
    return LoginToken(token= str(token))

