from pydantic import BaseModel
from pydantic.fields import Field

CartIDValidator = Field(..., title="ID do cart", ge=0, description="ID do Cart (deve ser único)")
UserIDValidator = Field(..., title="ID do usuário", ge=0, description="ID do User (deve ser único)")
ProdNameValidator = Field(..., title="Nome do Produto", min_length=2, max_length=30, description="Nome do produto (deve ser único)")
QuantValidator = Field(..., title="Quantidade do produto", ge=1, description="Quantidade de um produto")


class ORMMode(BaseModel):
    class Config:
        orm_mode = True


class Cart(ORMMode):
    cart_id: int = CartIDValidator 
    user_id: int = UserIDValidator


class CartCreation(ORMMode):
    user_id: int


class CartProduct(ORMMode):
    cart_id: int = CartIDValidator 
    name: str = ProdNameValidator
    quantity: int = QuantValidator


class CartProductUpdate(ORMMode):
    quantity: int
    name: str
