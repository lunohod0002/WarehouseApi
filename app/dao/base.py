from app.backend.db import async_session_maker, get_db
from sqlalchemy import select, insert


class BaseDAO():
    model = None

    @classmethod
    async def get_by_id(cls, id: int):
        async with async_session_maker() as session:
            result = await session.execute(select(cls.model.__table__.columns).where(cls.model.id==id))
            return result.mappings().one_or_none()

    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            result = await session.execute(select(cls.model.__table__.columns))
            print(result.mappings())
            return result.mappings().all()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            result=await session.execute(insert(cls.model).values(**data).returning(cls.model.id))
            await session.commit()
            return result.scalar()