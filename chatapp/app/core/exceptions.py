from fastapi.exceptions import HTTPException , WebSocketException
from fastapi import status

class HttpForbidden(HTTPException):
    def __init__(self):
        super().__init__(status_code = status.HTTP_403_FORBIDDEN)


class HttpUnauthorized(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED)


class WebsocketUnauthorized(WebSocketException):
    def __init__(self):
        super().__init__(code=status.WS_1008_POLICY_VIOLATION)
