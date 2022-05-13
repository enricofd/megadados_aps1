from ctypes import Union
from types import NoneType
from typing import List

from models.cart import Cart, CartCreation
from mysqlx import Session


class CartInterface:
    @staticmethod
    def get_carts(db: Session,) -> List[Cart]:
        pass

    @staticmethod
    def get_cart(db: Session, cart_id: int) -> Union[Cart, NoneType]:
        pass

    @staticmethod
    def create_cart(db: Session, cart_creation: CartCreation) -> Union[Cart, NoneType]:
        pass

    @staticmethod
    def delete_cart(db: Session, cart_id: str) -> Union[Cart, NoneType]:
        pass
