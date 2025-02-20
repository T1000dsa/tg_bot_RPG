from database_data.database import sync_engine, sync_session, async_engine, async_session, Base
from database_data.models import TgUsersModel, ScoreModel
from sqlalchemy import select, update, func, cast,Integer, and_, text, delete
from sqlalchemy.orm import aliased, joinedload, selectinload

async def init():
    async with async_engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()

async def insert_data(data):
   async with async_session() as session:
        if isinstance(data, TgUsersModel):
            session.add(data)
            await session.commit()

        elif isinstance(data, ScoreModel):
            session.add(data)
            await session.commit()


async def change_data(data:int|str, score:int):
    async with async_session() as session:
        if isinstance(data, int):
            statement = (
                update(ScoreModel)
                .where(ScoreModel.parent_id == data)
                .values(score=score)
                )
            await session.execute(statement)
            await session.commit()
        else:
            statement = (
                    update(ScoreModel)
                    .where(TgUsersModel.user_id==data)
                    .values(score=score)
                    )
            await session.execute(statement)
            await session.commit()



async def output_data():
   async with async_session() as session:
        query = select(TgUsersModel)
        res = await session.execute(query)
        result = res.scalars().all()
        return result


async def drop_object(id:int=None):
    if id is None:
        async with async_engine.connect() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.commit()
    else:
        async with async_session() as session:
            statement = (
                    delete(TgUsersModel)
                    .where(TgUsersModel.id == id)
                )
            await session.execute(statement)
            await session.commit()

    