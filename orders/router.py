from typing import List
from fastapi import status, HTTPException
from fastapi import APIRouter
from app.orders.dao import OrdersDao, OrderItemsDao
from app.products.dao import ProductsDao
from app.orders.service import OrderService
router = APIRouter(prefix="/orders",
                   tags=['Orders'])
from app.orders.schemas import SOrder, CreateOrderItem,CreateOrder


@router.get("")
async def get_all():
    return await OrderService.get_all()


@router.post("/create")
async def create_order(orderItems: CreateOrder):
    await OrderService.create_order(orderItems)



@router.get("/{id}")
async def get_order(id: int):
    order = await OrderService.get_order(id)
    return order


@router.patch("/{id}/{status}")
async def update_status(id: int, status: str):
    return await OrderService.update_status(id, status)
