from app.dao.base import BaseDAO
from app.Product import Products
from sqlalchemy import update,delete
from app.database import async_session_maker
from app.Product.schemas import SProduct
class ProductsDao(BaseDAO):
    model = Products
    @classmethod
    async def update_product(cls, id, update_product:SProduct):
        async with async_session_maker() as session:
            await session.execute(update(cls.model).where(Products.id == id).values(
            name=update_product.name,
            description=update_product.description,
            price=update_product.price,
            number=update_product.number))
            await session.commit()

    @classmethod
    async def delete_product(cls, id):
        async with async_session_maker() as session:
            await session.execute(delete(cls.model).where(Products.id == id))
            await session.commit()
    @classmethod
    async def update_number(cls, id, number):
        async with async_session_maker() as session:
            await session.execute(update(cls.model).where(Products.id == id).values(
                number=number))
            await session.commit()
