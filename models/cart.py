from pydantic import BaseModel

class Cart(BaseModel):
    cart_id: int
    user_id: int

class CartCreation(BaseModel):
    user_id: int
    
class CartNoID(BaseModel):
    user_id: int

class CartProduct(BaseModel):
    cart_id: int
    product_name: str
    quantity: int

class CartProductNoID(BaseModel):
    product_name: str
    quantity: int