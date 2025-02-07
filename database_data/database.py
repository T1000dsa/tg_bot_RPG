from sqlalchemy import create_engine, String, BIGINT
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker 
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

async_engine = create_async_engine(
    settings.DATABASE_URL_asyncpg,
    echo=True
)

sync_session = sessionmaker(sync_engine)
async_session = async_sessionmaker(async_engine)