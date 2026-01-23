from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from redis.asyncio import Redis


class WSRedis(ABC):
    """Redis abstract class."""

    @staticmethod
    @abstractmethod
    def fetch_data(uid: str, redis: Redis) -> Optional[Dict]:
        """Stores data in the Redis database.
        Args:
            uid (str): The user's id.
            redis : The Redis instance.
        Returns:
            Dict : The dict containing info of the connected user
        """

    @staticmethod
    @abstractmethod
    def store_data(data: Dict, redis: Redis):
        """fetch data from the redis database.
        Args:
            data (Dict): The dict containing info of the connected user.
            redis : The Redis instance.

        Returns:
            None : Return None.
        """

    @staticmethod
    @abstractmethod
    def remove_data(uid: str, redis: Redis):
        """delete data from the Redis database.
        Args:
            uid (str): The id of the user.
            redis : The Redis instance.

        Returns:
            Bool : Return true if the action succeed and false otherwise.
        """
