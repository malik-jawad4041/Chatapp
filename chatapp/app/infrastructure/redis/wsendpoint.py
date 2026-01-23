import json
from typing import Dict, Optional

from redis.asyncio import Redis

from chatapp.app.infrastructure.Redis import WSRedis


class RepoRedis(WSRedis):
    """
    RepoRedis is a Redis repository class that provides static methods
    to interact with Redis for storing, fetching, and removing data.
    Inherits from WSRedis.
    """

    @staticmethod
    async def fetch_data(uid: str, red: Redis) -> Optional[Dict]:
        """
        Fetch data from Redis for a given key.

        Args:
            uid (str): The key to fetch data from Redis.
            red (Redis): The Redis client instance.

        Returns:
            Optional[Dict]: The data as a dictionary if found, otherwise None.
        """
        data = await red.get(uid)
        if data is not None:
            return json.loads(data)
        return None

    @staticmethod
    async def store_data(data: Dict, red: Redis):
        """
        Store a dictionary in Redis.

        Args:
            data (Dict): The dictionary to store. Must contain an 'id' key for the Redis key.
            red (Redis): The Redis client instance.

        Returns:
            None
        """
        data = await red.set(data["id"], json.dumps(data))

    @staticmethod
    async def remove_data(uid: str, red: Redis):
        """
        Remove a key and its associated data from Redis.

        Args:
            uid (str): The key to delete from Redis.
            red (Redis): The Redis client instance.

        Returns:
            None
        """
        await red.delete(uid)
