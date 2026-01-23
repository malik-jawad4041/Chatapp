from fastapi import APIRouter ,Request , Response ,Header ,HTTPException
from chatapp.app.core.dependencies import IWS , DBSession ,key
from chatapp.app.core.exceptions import HttpUnauthorized
from typing import Annotated

ct_router = APIRouter()


@ct_router.post('/webhook')
async def centrifugo_proxy(request : Request, session :DBSession,x_api_key : Annotated[str,Header()]):
    """
        Proxy endpoint for receiving messages from Centrifugo and storing them in the database.

        This endpoint validates the provided API key and, if valid, extracts message data
        from the request payload and stores it using the `IWS.add_message` method.

        Args:
            request (Request): The incoming HTTP request containing JSON data.
            session (DBSession): Database session for interacting with the database.
            x_api_key (str, Header): API key provided in the request header for authentication.

        Raises:
            HttpUnauthorized: Raised if the provided API key does not match the expected secret key.

        Returns:
            Response: HTTP 200 OK response indicating successful message processing.
"""

    apikey = key()
    if x_api_key != apikey.secret_key:
        raise HttpUnauthorized()

    data = await request.json()
    await IWS.add_message(session,data.get('user'),data.get('data')['text'],data.get('channel'))
    return Response(status_code=200)
