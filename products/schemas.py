from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import date


class SProduct(BaseModel):
    id: int
    name: str
    description: str
    price: int
    number: int
    model_config = ConfigDict(from_attributes=True)
