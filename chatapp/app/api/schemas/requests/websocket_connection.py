from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
    id : str
    message : str
    name : Optional[str] = None
