from pydantic import BaseModel

class Product(BaseModel):
    price: float
    name: str
    description: str


class ProductNameless(BaseModel):
    price: float
    description: str
