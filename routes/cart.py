
from typing import List

from fastapi import APIRouter
from interfaces import CartInterface, CartProductInterface
from models.cart import Cart, CartCreation,  CartProduct,  CartProductUpdate
from fastapi.params import Body, Path

router = APIRouter(prefix='/cart')


@router.post("/")
async def create_cart(cart_creation: CartCreation = Body(..., example={
	"user_id": 1
})):
    cart = CartInterface.create_cart(cart_creation)
    return cart


@router.get("/", response_model=List[Cart])
async def get_carts():
    carts = CartInterface.get_carts()
    return carts


@router.get("/{cart_id}", response_model=List[CartProduct])
async def get_cart_products(cart_id: int = Path(..., example=2)):
    cart = CartProductInterface.get_cart_products(cart_id)
    return cart


@router.post("/{cart_id}", response_model=List)
async def add_to_cart(cart_id: int = Path(..., example=2), cart_product: CartProduct = Body({
	"cart_id": 0,
	"product_name": "batata2001",
	"quantity": 2
})):
    cart_product = CartProductInterface.add_to_cart(cart_id, cart_product)
    return cart_product


@router.delete("/{cart_id}", response_model=Cart)
async def delete_cart(cart_id: int = Path(..., example=2)):
    cart = CartInterface.delete_cart(cart_id)
    return cart


@router.delete("/{cart_id}/{item_name}", response_model=CartProduct)
async def delete_from_cart(cart_id: int = Path(..., example=2), item_name: str = Path(..., example="Beterraba")):
    cart_product = CartProductInterface.remove_product(
        cart_id, item_name)
    return cart_product


@router.patch("/{cart_id}", response_model=CartProduct)
async def update_product_cart(cart_id: int = Path(..., example=2),  cart_update: CartProductUpdate = Body(..., example={
	"product_name": "Beterraba",
	"quantity": 15
})):
    cart_product = CartProductInterface.update_quantity(cart_id, cart_update)
    return cart_product
