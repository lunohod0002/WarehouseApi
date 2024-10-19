from app.database import Base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

class Products(Base):
    __tablename__ = "product"
    id = Column(Integer, nullable=False, primary_key=True, index=True)
    name = Column(String,nullable=False)
    description = Column(String,nullable=False)
    price = Column(Integer,nullable=False)
    number = Column(Integer,nullable=False)

#print(CreateTable(Products.__table__))

#Base.metadata.create_all(bind=engine)
