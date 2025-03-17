from pydantic import BaseModel, field_validator
from typing import Optional


class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

    @field_validator('price')
    def validate_price(cls, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        return value

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    name: Optional[str] = None
    price: Optional[float] = None

class Item(ItemBase):
    id: int