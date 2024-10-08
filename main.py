from fastapi import FastAPI
from app.Product.router import router as product_order
from app.Order.router import router as oder_router

app=FastAPI()
app.include_router(router=product_order)
app.include_router(router=oder_router)