from database_data.database import sync_engine, sync_session, Base
from database_data.models import TgUsersORM, table_name
from sqlalchemy import select, update, func, cast,Integer, and_, text
from sqlalchemy.orm import aliased, joinedload, selectinload

def init():
    Base.metadata.create_all(sync_engine)

def insert_data(data:TgUsersORM):
    with sync_session() as session:
        session.add(data)
        session.commit()


def change_data(data):
    with sync_session() as session:
        pass


def output_data(data=None):
    with sync_session() as session:
        if data is None:
            query = text(f'SELECT * FROM {table_name}')
            result = session.execute(query).fetchall()
            return result
        else:
            query = text(data)
            result = session.execute(query).fetchall()
            return result


def drop_data(data=None):
    with sync_session() as session:
        if data is None:
            Base.metadata.drop_all(sync_engine)
            session.commit()
        else:
            query = text(data)
            session.execute(query)
            session.commit()

    