from pydantic import BaseModel


class Product(BaseModel):
    price: float
    name: str
    description: str
