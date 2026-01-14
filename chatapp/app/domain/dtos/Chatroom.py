
from dataclasses import dataclass
import datetime


@dataclass(frozen=True)
class ChatRoomDTO:
    id: str
    time : datetime.datetime
    message: str
    receiver: str

