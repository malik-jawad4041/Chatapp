from pydantic import BaseModel

class LoginToken(BaseModel):
    token : str



