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
        pass

    @staticmethod
    def get_cart(db: Session, cart_id: int) -> Optional[Cart]:
        pass

    @staticmethod
    def create_cart(db: Session, cart_creation: CartCreation) -> Optional[Cart]:
        pass

    @staticmethod
    def delete_cart(db: Session, cart_id: str) -> Optional[Cart]:
        pass
