from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

Base = declarative_base()


class Room(Base):
    __tablename__ = "room"
    id: Mapped[str] = mapped_column(String)
    time: Mapped[str] = mapped_column(DateTime, primary_key=True, default=datetime.now)
    message: Mapped[str] = mapped_column(String)
    receiver: Mapped[str] = mapped_column(String, default="all")


class Users(Base):
    __tablename__ = "userss"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    time: Mapped[str] = mapped_column(DateTime, default=datetime.now)
    username: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    roomid: Mapped[str] = mapped_column(String)
