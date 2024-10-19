import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("id,name,description,price,number,status_code",[
   (2,"Томаты","Лучшие томаты",200, 100,409),
    (3,"Огурцы","Лучшие огурцы",150, 200,409),
    (1,"Хлеб","Лучший хлеб",50, 80,409),
    (4,"Молоко","Лучшее молоко",50, 80,201),
])
async def test_create_product(id, name, description, price, number,status_code, ac: AsyncClient):
    response = await ac.post("/product", json={
        "id": id,
        "name": name,
        "description": description,
        "price": price,
        "number": number
    })
    print(response)
    assert response.status_code == status_code

@pytest.mark.parametrize("product,status_code", [
    ([{"product_id": 2, "products_number": 10}, {"product_id": 3, "products_number": 20}, {"product_id": 1, "products_number": 15}], 201),
    ([{"product_id": 2, "products_number": 100}, {"product_id": 3, "products_number": 200}, {"product_id": 1, "products_number": 150}], 404),
])
async def test_create_order(products,status_code, ac: AsyncClient):
    response = await ac.post("/order", json=products)
    assert response == status_code

@pytest.mark.parametrize("product,status_code", [
    ([{"product_id": 2, "products_number": 10}, {"product_id": 3, "products_number": 20}, {"product_id": 1, "products_number": 15}], 201),
    ([{"product_id": 2, "products_number": 100}, {"product_id": 3, "products_number": 200}, {"product_id": 1, "products_number": 150}], 404),
])
async def test_create_order(products,status_code, ac: AsyncClient):
    response = await ac.post("/order", json=products)
    print(response)
    assert response == status_code

