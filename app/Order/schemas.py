from typing import Optional, List

from pydantic import BaseModel, ConfigDict
from datetime import datetime
class SOrderItem(BaseModel):
    id: int
    order_id: int
    product_id: int
    products_number: int

    model_config = ConfigDict(from_attributes=True)
class SOrder(BaseModel):
    id: int
    creation_date: Optional[datetime]
    status: str
    orderItems: List[Optional[SOrderItem]]
    model_config = ConfigDict(from_attributes=True)

class CreateOrderItem(BaseModel):
    id: int
    product_id: int
    products_number: int

    model_config = ConfigDict(from_attributes=True)
