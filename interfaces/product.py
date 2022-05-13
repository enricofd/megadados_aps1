from ctypes import Union
from types import NoneType
from typing import List

from models.product import Product
from sqlalchemy.orm import Session


class ProductInterface:
    @staticmethod
    def get_products(db: Session) -> List[Product]:
        pass

    @staticmethod
    def get_product(db: Session, product_name: str) -> Union[Product, NoneType]:
        pass

    @staticmethod
    def create_product(db: Session, product: Product) -> Product:
        pass

    @staticmethod
    def update_product(db: Session, product_name: str, product_update: Product) -> Union[Product, NoneType]:
        pass

    @staticmethod
    def delete_product(db: Session, product_name: str) -> Union[Product, NoneType]:
        pass
