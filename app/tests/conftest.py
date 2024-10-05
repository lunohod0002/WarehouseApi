import asyncio

import pytest
from app.backend.db import Base,async_session_maker,engine
from app.config import settings
from app.backend.db import Base
from sqlalchemy import select,insert,update,delete
from main import app as fastapi_app
from app.Product import Products
from app.Order import Orders,OrderItems
import json
from fastapi.testclient import TestClient
from httpx import AsyncClient
@pytest.fixture(scope="session",autouse=True)
async def prepare_database():
    assert settings.MODE=="TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest.fixture(scope="session")
def event_loop(request):
    loop=asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac


