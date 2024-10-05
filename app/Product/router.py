from fastapi import status, HTTPException
from fastapi import APIRouter
from app.Product.dao import ProductsDao

router = APIRouter(prefix="/products",
                   tags=['Products'])
from app.Product.schemas import SProduct


@router.get("")
async def getAll() -> list[SProduct]:
    return await ProductsDao.get_all()


@router.post("")
async def createProduct(product: SProduct):
    exist_product =ProductsDao.get_by_id(id=product.id)
    if exist_product != None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Product is already exist!'
        )
    await ProductsDao.add(id=product.id, name=product.name, price=product.price, number=product.number,
                          description=product.description)
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Product was created!'
    }


@router.get("/{id}")
async def getProduct(id: int) :
    return await ProductsDao.get_by_id(id)


@router.put("/{id}")
async def updateProduct(id: int, updateProduct: SProduct):
    product = ProductsDao.get_by_id(id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no Product found!'
        )
    await ProductsDao.update_product(id, update_product=updateProduct)
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Product update is successful'
    }


@router.delete("/{id}")
async def deleteProduct(id: int):
    product = await ProductsDao.get_by_id(id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no Product found!'
        )
    await ProductsDao.delete_product(id=id)
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Product id deleted  successful!'
    }
