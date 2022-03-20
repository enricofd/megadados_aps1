from pydantic import BaseModel


class ProductCreation(BaseModel):
    price: float
    name: str
    description: str


class Product(ProductCreation):
    product_id: int
