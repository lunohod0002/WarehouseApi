from typing import List

from fastapi import HTTPException
from starlette import status

from app.products.schemas import SProduct
from app.products.dao import ProductsDao


class ProductService():
    @classmethod
    async def get_all(cls) -> List[SProduct]:
        return await ProductsDao.get_all()

    @classmethod
    async def create_product(cls, product: SProduct):
        exist_product = await ProductsDao.get_by_id(id=product.id)
        if exist_product != None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='products is already exist!'
            )
        await ProductsDao.add(id=product.id, name=product.name, price=product.price, number=product.number,
                              description=product.description)
        return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'products was created!'
        }

    @classmethod
    async def get_product(cls, id: int) -> SProduct:
        return await ProductsDao.get_by_id(id)

    @classmethod
    async def update_product(cls, id: int, updateProduct: SProduct):
        product = ProductsDao.get_by_id(id)
        if product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='There is no products found!'
            )
        await ProductsDao.update_product(id, update_product=updateProduct)
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'products update is successful'
        }

    @classmethod
    async def delete_product(cls, id: int):
        product = await ProductsDao.get_by_id(id)
        if product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='There is no products found!'
            )
        await ProductsDao.delete_product(id=id)
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'products id deleted  successful!'
        }
