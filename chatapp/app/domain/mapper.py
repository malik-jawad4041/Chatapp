from abc import ABC, abstractmethod
from typing import Generic, TypeVar

DB = TypeVar("DB")
DTO = TypeVar("DTO")


class Mapper(ABC, Generic[DB, DTO]):
    """Abstract base class for mapping between database models and DTOs.

    Provides a standard interface for converting:
        - a database model to a Data Transfer Object (DTO)
        - a DTO back to a database model.

    Type Parameters:
        DB: The type of the database model.
        DTO: The type of the Data Transfer Object.
    """

    @staticmethod
    @abstractmethod
    def to_dto(model: DB) -> DTO:
        """Convert a database model instance to a DTO.

        Args:
            model (DB): The database model instance.

        Returns:
            DTO: The corresponding Data Transfer Object.
        """

    @staticmethod
    @abstractmethod
    def from_dto(model: DTO) -> DB:
        """Convert a DTO back to a database model instance.

        Args:
            model (DTO): The Data Transfer Object.

        Returns:
            DB: The corresponding database model instance.
        """
