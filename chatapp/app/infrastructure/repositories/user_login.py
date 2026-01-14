'''



# this session belongs to infrastructure.repositories
async with session() as db:

    iid = 0
    name = ""
    stmt = select(database.Users).where(Users.username == body.username)
    result = await db.execute(stmt)
    a = result.scalars().first()


    if a is not None:
        iid = str(a.id)
        name = str(a.username)

        # This password check belongs to domain.services( abstract base class ) and its concrete derived class will be in the chatapp.services
        db_password = hashlib.sha256(body.password.encode())
        db_pass = db_password.hexdigest()
        if a.password != db_pass:

            # This HTTPException will be created in core.exceptions.py
            raise HttpUnauthorized()

    # This password hashing belongs to domain.services( abstract base class ) and its concrete derived class will be in the chatapp.services
    else:
        uid  = str(uuid.uuid4())
        username = body.username
        password = hashlib.sha256(body.password.encode())
        iid = uid
        name = username
        user = Users(username=username ,password=password.hexdigest() ,id=uid)
        db.add(user)
        await db.commit()

# the secret_key and algorithm will be passed to the domain.services
try:
    secret_ke y= settings.secret_key
    algorithm = settings.algorithm


    # the domain.services function will return tbe token
    payload = {
        "id" :iid,
        "username": name,
        "exp": datetime.now() + timedelta(minutes=30)  # token expires in 30 mins
    }
    token = jwt.encode(payload, secret_key, algorithm=algorithm)

    # this token will be returned in the router
    token = user_login.LoginToken(token=token)
    return token
finally:
    pass
'''

from sqlalchemy.ext.asyncio import AsyncSession
from chatapp.app.domain.dtos.user_login import LoginDTO
from ...infrastructure import db_modals
from sqlalchemy import select
from chatapp.app.domain.repositories.user_login import IUserLoginRepository
from ...infrastructure.mappers.user_login import Login
from chatapp.app.infrastructure.db_modals import Users



class UserLoginRepository(IUserLoginRepository):

    @staticmethod
    async def check_user_from_db(session : AsyncSession,body: LoginDTO):

        stmt = select(db_modals.Users).where(db_modals.Users.username == body.username)
        result = await session.execute(stmt)
        user = result.scalars().first()
        if not user:
            return None
        return Login.to_dto(user)

    @staticmethod
    async def add_user_to_db(session:AsyncSession,body: LoginDTO, uid:str) -> None:

        user = Users(username=body.username, password=body.password, id=uid)
        session.add(user)
        await session.flush()





