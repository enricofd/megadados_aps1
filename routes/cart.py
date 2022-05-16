from typing import List

from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends, HTTPException
from interfaces import CartInterface, CartProductInterface
from models.cart import Cart, CartCreation, CartProduct, CartProductUpdate
from fastapi.params import Body, Path
from database import get_db

router = APIRouter(prefix="/cart")


@router.post("/")
async def create_cart(
    db: Session = Depends(get_db),
    cart_creation: CartCreation = Body(..., example={"user_id": 1}),
):
    cart = CartInterface.create_cart(db, cart_creation)
    return cart


@router.get("/", response_model=List[Cart])
async def get_carts(db: Session = Depends(get_db)):
    carts = CartInterface.get_carts(db)
    return carts


@router.get("/{cart_id}", response_model=List[CartProduct])
async def get_cart_products(
    cart_id: int = Path(..., example=2), db: Session = Depends(get_db)
):
    cart = CartProductInterface.get_cart_products(db, cart_id)
    return cart


@router.post("/{cart_id}", response_model=CartProduct)
async def add_to_cart(
    cart_product: CartProduct = Body(
        {"cart_id": 0, "name": "batata2001", "quantity": 2}
    ),
    db: Session = Depends(get_db),
):
    product_in_cart = (
        CartProductInterface.get_cart_product(
            db, cart_product.cart_id, cart_product.name
        )
        is not None
    )

    if product_in_cart:
        raise HTTPException(400, "Product already in cart")

    cart_product = CartProductInterface.add_to_cart(db, cart_product)
    return cart_product


@router.delete("/{cart_id}")
async def delete_cart(
    cart_id: int = Path(..., example=2), db: Session = Depends(get_db)
):
    CartInterface.delete_cart(db, int(cart_id))


@router.delete("/{cart_id}/{item_name}", response_model=CartProduct)
async def delete_from_cart(
    cart_id: int = Path(..., example=2),
    item_name: str = Path(..., example="Beterraba"),
    db: Session = Depends(get_db),
):

    cart_product = CartProductInterface.remove_product(db, cart_id, item_name)
    return cart_product


@router.patch("/{cart_id}", response_model=CartProduct)
async def update_product_cart(
    cart_id: int = Path(..., example=2),
    cart_update: CartProductUpdate = Body(
        ..., example={"name": "Beterraba", "quantity": 15}
    ),
    db: Session = Depends(get_db),
):
    cart_product = CartProductInterface.update_quantity(db, cart_id, cart_update)
    return cart_product
