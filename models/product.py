from pydantic import BaseModel
from pydantic.fields import Field


PriceValidator = Field(..., title="Preço", ge=0, description="Preço de um produto")
NameValidator = Field(..., title="Nome", min_length=2, description="Nome de um produto") 
DescValidator = Field(..., title="Descrição", min_length=6, description="Descrição de um produto") 

class ORMMode(BaseModel):
    class Config:
        orm_mode = True

class Product(ORMMode):
    price: float = PriceValidator
    name: str = NameValidator
    description: str = DescValidator


class ProductNameless(ORMMode):
    price: float = PriceValidator
    description: str = DescValidator
