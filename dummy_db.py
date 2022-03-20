from models.product import Product
from fastapi import HTTPException


_product = {}


class ProductInterface:
    @staticmethod
    def get_product(product_name) -> Product:
        try:
            return Product(**_product.get(product_name))
        except:
            return None

    @staticmethod
    def create_product(product: Product):
        if product.name not in _product:
            _product[product.name] = product.dict()
            return ProductInterface.get_product(product.name)
        raise HTTPException(400, "Product already exists")
