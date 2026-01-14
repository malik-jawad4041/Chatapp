"""Mapper for converting between Users database models and UsersDTO objects.

Provides methods to transform data between the database representation
and the application's data transfer objects.
"""

from chatapp.app.domain.mapper import Mapper

from ...domain.dtos.Users import UsersDTO
from ..db_modals import Users


class Login(Mapper[Users, UsersDTO]):
    """Mapper class for Users model and UsersDTO.

    Inherits from the generic Mapper interface.
    """

    @staticmethod
    def to_dto(model: Users) -> UsersDTO:
        """Converts a Users database model to a UsersDTO.

        Args:
            model (Users): Database model instance.

        Returns:
            UsersDTO: Data transfer object representation of the user.
        """
        dto = UsersDTO(
            id=model.id,  # type: ignore
            time=model.time,  # type: ignore
            username=model.username,  # type: ignore
            password=model.password,  # type: ignore
            roomid=model.roomid,  # type: ignore
        )
        return dto

    @staticmethod
    def from_dto(dto: UsersDTO) -> Users:
        """Converts a UsersDTO back to a Users database model.

        Args:
            dto (UsersDTO): Data transfer object instance.

        Returns:
            Users: Database model representation of the user.
        """
        model = Users(
            id=dto.id,
            time=dto.time,
            username=dto.username,
            password=dto.password,
            roomid=dto.roomid,
        )
        return model
