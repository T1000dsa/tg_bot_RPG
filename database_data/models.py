from database_data.database import Base, str_128, str_256
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import MetaData,Table, Column, Integer, String, ForeignKey, func, text, BIGINT, BLOB, BigInteger
from typing import Annotated

class TgUsersORM(Base):
    __tablename__ = 'tgbotusers'

    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[str_128]
    username:Mapped[str_128|None]
    firstname:Mapped[str_128|None]
    lastname:Mapped[str_128|None]
    bio:Mapped[str_256|None]
    is_bot:Mapped[bool|None]
    language_code:Mapped[str|None]
    
table_name = TgUsersORM.__tablename__