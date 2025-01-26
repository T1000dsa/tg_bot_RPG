from sqlalchemy import create_engine, String, BIGINT
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from database_data.database_settings import settings
from typing import Annotated

str_128 = Annotated[str, 128]
str_256 = Annotated[str, 256]

class Base(DeclarativeBase):
    type_annotation_map = {
        str_128: String(128),
        str_256: String(256),

    }

sync_engine = create_engine(
    settings.DATABASE_URL_psycopg,
    echo=True
    )

sync_session = sessionmaker(sync_engine)