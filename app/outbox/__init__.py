from app.database import Base
from sqlalchemy import Column, JSON
from sqlalchemy.types import Integer, String


class OutBox(Base):
    __tablename__ = "outbox"
    id = Column(Integer, nullable=False, primary_key=True)
    payload = Column(JSON,nullable=False)
    status = Column(String, nullable=False)
