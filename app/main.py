import multiprocessing
from contextlib import asynccontextmanager
from fastapi import FastAPI
import schedule
import asyncio
from app.products.router import router as product_router
from app.orders.router import router as oder_router
from app.outbox.service import background_task

process = multiprocessing.Process(target=background_task)


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(background_task())
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router=product_router)
app.include_router(router=oder_router)
