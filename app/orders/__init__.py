from app.database import Base
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
    idempotency_key=Column(String,unique=True)
    items = relationship(lambda: OrderItems, foreign_keys=lambda: OrderItems.order_id,backref='order_items')
class OrderItems(Base):
    __tablename__ = "order_items"
    id = Column(Integer, nullable=False, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    products_number=Column(Integer,nullable=False)
class IdempotencyKey(Base):
    __tablename__ = "idempotency_key"
    id = Column(Integer, nullable=False, primary_key=True, index=True)
    idempotency_key=Column(String,unique=True)






'''async def create_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
run(create_tables())'''