"""Mapper for converting between Room database models and ChatRoomDTO objects.

Provides methods to transform data between the database representation
and the application's data transfer objects.
"""

from chatapp.app.domain.mapper import Mapper

from chatapp.app.domain.dtos.Chatroom import ChatRoomDTO
from chatapp.app.infrastructure.db_modals import Room


class WSMapper(Mapper[Room, ChatRoomDTO]):
    """Mapper class for Room model and ChatRoomDTO.

    Inherits from the generic Mapper interface.
    """

    @staticmethod
    def to_dto(model: Room) -> ChatRoomDTO:
        """Converts a Room database model to a ChatRoomDTO.

        Args:
            model (Room): Database model instance.

        Returns:
            ChatRoomDTO: Data transfer object representation of the chat room message.
        """
        dto = ChatRoomDTO(
            id=model.id,  # type: ignore
            time=model.time,  # type: ignore
            message=model.message,  # type: ignore
            receiver=model.receiver,  # type: ignore
        )
        return dto

    @staticmethod
    def from_dto(dto: ChatRoomDTO) -> Room:
        """Converts a ChatRoomDTO back to a Room database model.

        Args:
            dto (ChatRoomDTO): Data transfer object instance.

        Returns:
            Room: Database model representation of the chat room message.
        """
        model = Room(
            id=dto.id,
            time=dto.time,
            message=dto.message,
            receiver=dto.receiver,
        )
        return model
