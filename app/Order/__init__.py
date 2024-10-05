import enum

from app.backend.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String,DateTime
from sqlalchemy.sql import func
'''import enum
from  sqlalchemy.types import Enum
class OrderStatus(enum.Enum):
    IN_PROGRESS="in progress"
    DELIVERED="delivered"
    SENT="sent"
    
OrderStatusType: Enum = Enum(
    PostStatus,
    name="post_status_type",
    create_constraint=True,
    metadata=Base.metadata,
    validate_strings=True,
)'''
class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, nullable=False, primary_key=True, index=True)
    creation_date = Column(DateTime,default=func.now())
    status = Column(String,nullable=False)
    items = relationship(lambda: OrderItems, foreign_keys=lambda: OrderItems.order_id,backref='order_items')
class OrderItems(Base):
    __tablename__ = "order_items"
    id = Column(Integer, nullable=False, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    products_number=Column(Integer,nullable=False)

'''async def create_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
run(create_tables())'''