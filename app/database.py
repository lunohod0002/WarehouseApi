from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession,async_sessionmaker
from sqlalchemy.orm import sessionmaker, DeclarativeBase,create_session
from app.config import settings

if (settings.MODE=="TEST"):
    DATABASE_URL=f"postgresql+asyncpg://{settings.TEST_DB_USER}:{settings.TEST_DB_PASS}@{settings.TEST_DB_HOST}:{settings.TEST_DB_PORT}/{settings.TEST_DB_NAME}"
    DATABASE_PARAMS={"poolclass":NullPool}
else:
    DATABASE_URL=f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
    DATABASE_PARAMS={}

engine = create_async_engine(DATABASE_URL,**DATABASE_PARAMS)

async_session_maker=async_sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=False)
engine.connect()
async def get_db() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
class Base(DeclarativeBase):
    pass

