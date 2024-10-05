from typing import List
from fastapi import status, HTTPException
from fastapi import APIRouter
from app.Order.dao import OrdersDao, OrderItemsDao
from app.Product.dao import ProductsDao

router = APIRouter(prefix="/orders",
                   tags=['Orders'])
from app.Order.schemas import SOrder, CreateOrderItem


@router.get("")
async def getAll():
    return await OrdersDao.get_all()


@router.post("/create")
async def createOrder(orderItems: list[CreateOrderItem]):
    products = {}

    for orderItem in orderItems:
        print(await ProductsDao.get_by_id(id=orderItem.product_id))
        product = await ProductsDao.get_by_id(id=orderItem.product_id)
        products[product["id"]] = int(product["number"])

        if (product.number < orderItem.products_number):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'There is no products amount of {product["name"]}'
            )
    order_id = await OrdersDao.add(status="IN_PROGRESS")
    for orderItem in orderItems:
        await ProductsDao.update_number(id=orderItem.product_id,
                                        number=products[orderItem.product_id] - int(orderItem.products_number))
        await OrderItemsDao.add(id=orderItem.id, order_id=order_id, product_id=orderItem.product_id,
                                products_number=orderItem.products_number)

    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': f'Order {order_id} was created!'
    }


@router.get("/{id}")
async def getOrder(id: int):
    order = await OrdersDao.get_by_id(id)
    return order


@router.patch("/{id}/{status}")
async def updateStatus(id: int, status: str):
    return await OrdersDao.update_status(id, status)
