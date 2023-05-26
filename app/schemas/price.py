import datetime
from pydantic import BaseModel


class BasePrice(BaseModel):
    price: float
    timestamp: datetime.datetime


class PriceOut(BasePrice):
    id: int

    class Config:
        orm_mode = True
