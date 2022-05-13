from typing import List

from models.cart import CartProduct
from mysqlx import Session


class CartProductInterface:
    @staticmethod
    def get_cart_product(db: Session, cart_id: int, product_name: str) -> CartProduct:
        pass

    @staticmethod
    def get_cart_products(db: Session, cart_id: int) -> List:
        pass

    @staticmethod
    def add_to_cart(db: Session, cart_id: int, cart_product: CartProduct) -> CartProduct:
        pass

    @staticmethod
    def update_quantity(db: Session, cart_id: int, cart_update: CartProduct) -> List:
        pass

    @staticmethod
    def remove_product(db: Session, cart_id: int, product_name: str) -> CartProduct:
        pass
