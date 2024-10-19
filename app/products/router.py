from fastapi import status, HTTPException
from fastapi import APIRouter
from app.products.dao import ProductsDao
from app.products.service import ProductService

router = APIRouter(prefix="/products",
                   tags=['Products'])
from app.products.schemas import SProduct


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
