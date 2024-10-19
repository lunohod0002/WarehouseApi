from typing import List

from fastapi import HTTPException
from starlette import status

from app.orders.dao import OrdersDao, OrderItemsDao,IdempotencyKeyDao
from app.orders.schemas import CreateOrder
from app.orders.schemas import SOrder
from app.products.dao import ProductsDao


class OrderService():
    @classmethod
    async def get_all(cls) -> List[SOrder]:
        return await OrdersDao.get_all()

    @classmethod
    async def create_order(cls,orderItems: CreateOrder):
        products = {}
        idempotency_key = orderItems.idempotency_key
        for orderItem in orderItems.orderItems:
            print(await ProductsDao.get_by_id(id=orderItem.product_id))
            product = await ProductsDao.get_by_id(id=orderItem.product_id)
            print(product)
            products[product["id"]] = int(product["number"])

            if (product.number < orderItem.products_number):
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f'There is no products amount of {product["name"]}'
                )
            try:
                await IdempotencyKeyDao.add(idempotency_key=idempotency_key)

                order_id = await OrdersDao.add(status="IN_PROGRESS")
                for orderItem in orderItems.orderItems:
                    await ProductsDao.update_number(id=orderItem.product_id,
                                                    number=products[orderItem.product_id] - int(
                                                        orderItem.products_number))
                await OrderItemsDao.add(id=orderItem.id, order_id=order_id, product_id=orderItem.product_id,
                                        products_number=orderItem.products_number)
                return {
                    'status_code': status.HTTP_201_CREATED,
                    'transaction': f'Order {order_id} was created!'
                }
            except Exception as e:
                print(e)
                return {
                    'status_code': status.HTTP_200_OK,
                    'transaction': f'Order  was created!'
                }

    @classmethod
    async def get_order(cls,id: int):
        order = await OrdersDao.get_by_id(id)
        return order
    @classmethod
    async def update_status(cls,id: int, status: str):
        return await OrdersDao.update_status(id, status)

