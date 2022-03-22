from urllib import response

from numpy import quantile
from fastapi import APIRouter
from interfaces import CartInterface, CartProductInterface
from typing import Dict, List
from models.cart import Cart, CartProduct, CartProductNoID, CartNoID, CartCreation
from models.product import Product
from fastapi.params import Path, Body


router = APIRouter(prefix='/cart')

# /cart
# - POST: criar
@router.post("/", tags=["cart"])
async def create_cart(cart_creation: CartCreation = Body(
    ...,
    example = {"user_id": 1}
)):
    cart = CartInterface.create_cart(cart_creation)
    return cart

# - GET: listar carrinhos
@router.get("/", response_model=List[Cart])
async def get_carts():
    carts = CartInterface.get_carts()
    return carts

# /cart/:cart_id/
# - GET: listar produtos em um cart
@router.get("/{cart_id}", response_model=List[CartProduct])
async def get_cart_products(cart_id: int = Path(..., example=2)):
    cart = CartProductInterface.get_cart_products(cart_id)
    return cart

# - POST: adicionar item x quantidade
@router.post("/{cart_id}", response_model=List)
async def add_to_cart(cart_id: int = Path(..., example=2), cart_product: CartProduct = Body({
	"cart_id": 0,
	"product_name": "batata2001",
	"quantity": 2
})):
    cart_product = CartProductInterface.add_to_cart(cart_id, cart_product)
    return cart_product

# - PATCH: editar cart
@router.patch("/{cart_id}", response_model=CartNoID)
async def update_cart(cart_id: int = Path(..., example=2), cart_update: CartNoID = Body(
    {
	"cart_id": 0,
	"product_name": "batata2001",
	"quantity": 4
}
)):
    cart_product = CartInterface.update_cart(cart_id, cart_update)
    return cart_product

# - DELETE: deletar cart (itens também)
@router.delete("/{cart_id}", response_model=CartProduct)
async def delete_cart(cart_id: int = Path(..., example=2)):
    cart_product = CartProductInterface.delete_cart_products(cart_id)
    cart = CartInterface.delete_cart(cart_id)
    return cart, cart_product

# /cart/:id_cart/:id_item
# - DELETE: remover item
@router.delete("/{cart_id}/{item_name}", response_model=CartProduct)
async def delete_from_cart(cart_id: int = Path(..., example=2), item_name: str = Path(..., example="Beterraba")):
    cart_product = CartProductInterface.delete_cart_products(cart_id, item_name)
    return cart_product


# - PATCH: editar quantidade
@router.patch("/{cart_id}/{item_name}", response_model=CartProductNoID)
async def update_product_cart(cart_id: int = Path(..., example=2), cart_update: CartProductNoID = Path(..., example=2)):
    cart_product = CartProductInterface.update_cart_products(cart_id = Path(..., example=2), cart_update = Path(..., example=Body(..., example = {})))
    return cart_product 
