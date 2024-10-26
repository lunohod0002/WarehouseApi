
from app.dao.base import BaseDAO
from app.outbox import OutBox
from sqlalchemy import update,delete,select
from app.database import async_session_maker
class OutBoxDao(BaseDAO):
    model = OutBox
    @classmethod
    async def get_all_pending(cls):
        async with async_session_maker() as session:
            result = await session.execute(
                select(cls.model.__table__.columns).filter_by(status="CREATED").order_by(OutBox.id))
            return result.mappings().all()

    @classmethod
    async def update_status(cls, id):
        async with async_session_maker() as session:
            await session.execute(update(cls.model).where(OutBox.id == id).values(
                status="PROCESSED"))
            await session.commit()