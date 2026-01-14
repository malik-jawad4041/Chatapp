from chatapp.app.domain.mapper import Mapper
from ..db_modals import Users
from ...domain.dtos.Users import UsersDTO

class Login(Mapper[Users, UsersDTO]):


    @staticmethod
    def to_dto(model : Users) ->UsersDTO:
        dto = UsersDTO(
            id = model.id, # type: ignore
            time=model.time, # type: ignore
            username = model.username, # type: ignore
            password=model.password, # type: ignore
            roomid= model.roomid , # type: ignore
        )
        return dto


    @staticmethod
    def from_dto(dto : UsersDTO) -> Users:
        model = Users(
            id = dto.id,
            time = dto.time,
            username = dto.username,
            password = dto.password,
            roomid = dto.roomid,
        )
        return model



