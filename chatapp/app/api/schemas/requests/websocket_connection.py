from typing import Optional

from pydantic import BaseModel


class Message(BaseModel):
    """Pydantic model representing a chat message.

    Attributes:
        id (str): Unique identifier for the message.
        message (str): The content of the message.
        name (Optional[str]): Optional name of the sender.
    """

    id: str
    message: str
    name: Optional[str] = None
