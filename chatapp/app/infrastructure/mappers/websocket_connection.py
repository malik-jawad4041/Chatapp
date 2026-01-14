from chatapp.app.domain.mapper import Mapper
from ..db_modals import Room
from ...domain.dtos.Chatroom import ChatRoomDTO

class WSMapper(Mapper[Room,ChatRoomDTO]):


    @staticmethod
    def to_dto(model : Room) ->ChatRoomDTO:
        dto = ChatRoomDTO(
            id = model.id, # type: ignore
            time=model.time, # type: ignore
            message = model.message, # type: ignore
            receiver = model.receiver, # type: ignore
        )
        return dto


    @staticmethod
    def from_dto(dto : ChatRoomDTO) -> Room:
        model = Room(
            id = dto.id,
            time = dto.time,
            message = dto.message,
            receiver = dto.receiver,
        )
        return model

