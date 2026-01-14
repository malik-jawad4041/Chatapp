import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class ChatRoomDTO:
    """Data Transfer Object representing a chat message in a chat room.

    Attributes:
        id (str): Unique identifier of the sender or the message.
        time (datetime.datetime): Timestamp when the message was sent.
        message (str): Content of the chat message.
        receiver (str): Identifier of the message recipient or chat room.
    """
    id: str
    time: datetime.datetime
    message: str
    receiver: str
