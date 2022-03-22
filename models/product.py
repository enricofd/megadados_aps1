from matplotlib.cbook import file_requires_unicode
from pydantic import BaseModel
from pydantic.fields import Field


PriceValidator = Field(..., title="Preço", ge=0, description="Preço de um produto")
NameValidator = Field(..., title="Nome", min_length=2, description="Nome de um produto") 
DescValidator = Field(..., title="Descrição", min_length=6, description="Descrição de um produto") 


class Product(BaseModel):
    price: float = PriceValidator
    name: str = NameValidator
    description: str = DescValidator


class ProductNameless(BaseModel):
    price: float = PriceValidator
    description: str = DescValidator
