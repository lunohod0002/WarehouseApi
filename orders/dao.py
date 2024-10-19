from sqlalchemy.orm import selectinload

from app.dao.base import BaseDAO
from app.orders import Orders, OrderItems
from sqlalchemy import select, update
from app.database import async_session_maker

class OrdersDao(BaseDAO):
    model = Orders

    @classmethod
    async def update_status(cls, id, status):
        async with async_session_maker() as session:
            await session.execute(update(cls.model).where(Orders.id == id).values(
                status=status))
            await session.commit()

    @classmethod
    async def get_by_id(cls, id: int):
        async with async_session_maker() as session:
            result = await session.execute(select(cls.model.__table__.columns).filter_by(id=id).options(selectinload(Orders.items)))
            return result.mappings().all()
    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            result = await session.execute(select(cls.model.__table__.columns).options(selectinload(Orders.items)))
            return result.mappings().all()

class OrderItemsDao(BaseDAO):
    model = OrderItems
