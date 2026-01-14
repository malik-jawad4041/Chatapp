from abc import ABC, abstractmethod
from typing import Generic , TypeVar

DB = TypeVar("DB")
DTO = TypeVar("DTO")

class Mapper(ABC, Generic[DB,DTO]):
    """ This is an abstract mapper class """
    @staticmethod
    @abstractmethod
    def to_dto(model : DB)->DTO: ...

    @staticmethod
    @abstractmethod
    def from_dto(model: DTO)->DB: ...


