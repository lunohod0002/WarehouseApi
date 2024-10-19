from fastapi import status, HTTPException
from fastapi import APIRouter
from app.product.dao import ProductsDao
from app.product.service import ProductService

router = APIRouter(prefix="/product",
                   tags=['Products'])
from app.product.schemas import SProduct


@router.get("")
async def getAll() -> list[SProduct]:
    return await ProductService.getAll()


@router.post("")
async def create_product(product: SProduct):
    await ProductService.createProduct(product)


@router.get("/{id}")
async def get_product(id: int):
    return await ProductService.getProduct(id)


@router.put("/{id}")
async def update_product(id: int, updateProduct: SProduct):
    await ProductService.updateProduct(id, updateProduct=updateProduct)


@router.delete("/{id}")
async def delete_product(id: int):
    await ProductsDao.delete_product(id)
