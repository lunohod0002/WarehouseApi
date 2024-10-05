import asyncio

import pytest
from app.database import engine
from app.config import settings
from app.database import Base
from main import app as fastapi_app
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


