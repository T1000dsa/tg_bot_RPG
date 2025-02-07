from database_data.database import sync_engine, sync_session, async_engine, async_session, Base
from database_data.models import TgUsersORM, table_name
from sqlalchemy import select, update, func, cast,Integer, and_, text
from sqlalchemy.orm import aliased, joinedload, selectinload

async def init():
    async with async_engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()

async def insert_data(data:TgUsersORM):
   async with async_session() as session:
        session.add(data)
        session.commit()


async def change_data(data):
    async with async_session() as session:
        pass


async def output_data(data=None):
   async with async_session() as session:
        if data is None:
            query = text(f'SELECT * FROM {table_name}')
            result = await session.execute(query)
            result = result.fetchall()
            return result
        else:
            query = text(data)
            result = await session.execute(query)
            result = result.fetchall()
            return result


async def drop_data(data=None):
    async with async_engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()
    async with async_engine.connect() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.commit()

    