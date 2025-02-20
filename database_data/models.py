from database_data.database import Base, str_128, str_256
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import MetaData,Table, Column, Integer, String, ForeignKey, func, text, BIGINT, BLOB, BigInteger
from typing import Annotated
from datetime import datetime 


created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=datetime.now)]

class TgUsersModel(Base):
    __tablename__ = 'tgbotusers'

    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[str_128] = mapped_column(unique=True)
    username:Mapped[str_128|None]
    firstname:Mapped[str_128|None]
    lastname:Mapped[str_128|None]
    bio:Mapped[str_256|None]
    is_bot:Mapped[bool|None]
    language_code:Mapped[str|None]
    created_at:Mapped[created_at]
    updated_at:Mapped[updated_at]

    score:Mapped['ScoreModel'] = relationship(back_populates="tg_user")

class ScoreModel(Base):
    __tablename__ = 'scores'

    id:Mapped[int] = mapped_column(primary_key=True)
    parent_id:Mapped[str_128|None] = mapped_column(ForeignKey("tgbotusers.user_id", ondelete="CASCADE"))
    score:Mapped[int|None]

    tg_user:Mapped['TgUsersModel'] = relationship(back_populates="score")