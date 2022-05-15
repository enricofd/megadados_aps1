from ctypes import Union
from types import NoneType
from typing import Optional, List

from models.cart import Cart, CartCreation
from schemas.cart import Cart as CartSchema
from sqlalchemy.orm.session import Session


class CartInterface:
    @staticmethod
    def get_carts(
        db: Session,
    ) -> List[Cart]:
        return db.query(CartSchema).all()

    @staticmethod
    def get_cart(db: Session, cart_id: int) -> Optional[Cart]:
        return db.query(CartSchema).filter(CartSchema.id_cart == cart_id).first()

    @staticmethod
    def create_cart(db: Session, cart_creation: CartCreation) -> Optional[Cart]:
        cart = CartSchema(**cart_creation.dict())
        db.add(cart)
        db.commit()
        db.refresh(cart)
        return cart

    @staticmethod
    def delete_cart(db: Session, cart_id: str) -> Optional[Cart]:
        return db.query(CartSchema).filter(CartSchema.id_cart == cart_id).delete()
