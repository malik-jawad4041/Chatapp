from dataclasses import dataclass


@dataclass()
class PayloadDTO:
    """Data Transfer Object representing a JWT payload.

    Attributes:
        id (str): Unique identifier of the user.
        username (str): Username of the user.
    """

    id: str
    username: str
