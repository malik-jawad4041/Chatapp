import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class UsersDTO:
    """Data Transfer Object for a user.

    Attributes:
        id (int): Unique identifier for the user.
        time (datetime.datetime): Timestamp when the user was created.
        username (str): Username of the user.
        password (str): Hashed password of the user.
        roomid (str): Identifier for the chat room the user belongs to.
    """

    id: int
    time: datetime.datetime
    username: str
    password: str
    roomid: str
