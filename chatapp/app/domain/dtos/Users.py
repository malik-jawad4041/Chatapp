from dataclasses import dataclass
import datetime


@dataclass(frozen=True)
class UsersDTO:
    id: int
    time : datetime.datetime
    username: str
    password: str
    roomid : str
