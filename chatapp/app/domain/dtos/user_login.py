from dataclasses import dataclass


@dataclass()
class LoginDTO:
    """Data Transfer Object for user login credentials.

    Attributes:
        username (str): The username of the user.
        password (str): The password of the user.
    """
    username: str
    password: str
