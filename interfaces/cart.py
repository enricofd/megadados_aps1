from ctypes import Union
from types import NoneType
from typing import Optional, List

from models.cart import Cart, CartCreation
from sqlalchemy.orm.session import Session


class CartInterface:
    @staticmethod
    def get_carts(
        db: Session,
    ) -> List[Cart]:
        return db.query(Cart).all()

    @staticmethod
    def get_cart(db: Session, cart_id: int) -> Optional[Cart]:
        return db.query(Cart).filter(Cart.id == cart_id).first()

    @staticmethod
    def create_cart(db: Session, cart_creation: CartCreation) -> Optional[Cart]:
        cart = Cart(**cart_creation)
        db.add(cart)
        db.commit()
        db.refresh(cart)
        return cart

    @staticmethod
    def delete_cart(db: Session, cart_id: str) -> Optional[Cart]:
        return db.query(Cart).filter(Cart.id == cart_id).delete()
