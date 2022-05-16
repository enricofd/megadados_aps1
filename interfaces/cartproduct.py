from typing import List
from interfaces import cart

import schemas
from models.cart import CartProduct
from mysqlx import Session


class CartProductInterface:
    @staticmethod
    def get_cart_product(db: Session, cart_id: int, product_name: str) -> CartProduct:
        return (
            db.query(schemas.CartProduct)
            .filter(
                schemas.CartProduct.cart_id == cart_id,
                schemas.CartProduct.name == product_name,
            )
            .first()
        )

    @staticmethod
    def get_cart_products(db: Session, cart_id: int) -> List:
        return (
            db.query(schemas.CartProduct)
            .filter(schemas.CartProduct.cart_id == cart_id)
            .all()
        )

    @staticmethod
    def add_to_cart(db: Session, cart_product: CartProduct) -> CartProduct:
        cart_product = schemas.CartProduct(**cart_product.dict())
        db.add(cart_product)
        db.commit()
        db.refresh(cart_product)
        return cart_product

    @staticmethod
    def update_quantity(db: Session, cart_id: int, cart_update: CartProduct) -> List:
        db.query(schemas.CartProduct).filter(
            schemas.CartProduct.cart_id == cart_id
        ).update(cart_update.dict(), synchronize_session="fetch")
        db.commit()
        return CartProductInterface.get_cart_product(db, cart_id, cart_update.name)

    @staticmethod
    def remove_product(db: Session, cart_id: int, product_name: str):
        product = (
            db.query(schemas.CartProduct)
            .filter(
                schemas.CartProduct.cart_id == cart_id,
                schemas.CartProduct.name == product_name,
            )
            .first()
        )
        if product is not None:
            db.delete(product)
            db.commit()
