"""Custom HTTP and WebSocket exceptions for the application.

Defines specific exception classes for handling forbidden and
unauthorized access in HTTP and WebSocket contexts.
"""

from fastapi import status
from fastapi.exceptions import HTTPException, WebSocketException


class HttpForbidden(HTTPException):
    """Exception raised when an HTTP request is forbidden (403)."""

    def __init__(self):
        """Initialize the exception with HTTP 403 status code."""
        super().__init__(status_code=status.HTTP_403_FORBIDDEN)


class HttpUnauthorized(HTTPException):
    """Exception raised when an HTTP request is unauthorized (401)."""

    def __init__(self):
        """Initialize the exception with HTTP 401 status code."""
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED)


class WebsocketUnauthorized(WebSocketException):
    """Exception raised when a WebSocket connection is unauthorized."""

    def __init__(self):
        """Initialize the exception with WebSocket policy violation code (1008)."""
        super().__init__(code=status.WS_1008_POLICY_VIOLATION)
