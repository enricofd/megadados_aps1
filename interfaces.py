from models.product import Product
from fastapi import HTTPException
from typing import List

_product = {}


class ProductInterface:
    @staticmethod
    def get_products() -> List:
        return [Product(**product) for product in _product.values()]

    @staticmethod
    def get_product(product_name: str) -> Product:
        try:
            return Product(**_product[product_name])
        except:
            raise HTTPException(404, "Product not found")

    @staticmethod
    def create_product(product: Product):
        if product.name not in _product:
            _product[product.name] = product.dict()
            return ProductInterface.get_product(product.name)
        raise HTTPException(400, "Product already exists")

    @staticmethod
    def update_product(product_name: str, product_update: Product) -> Product:
        if product_name in _product:
            _product[product_name].update(product_update.dict())
            return ProductInterface.get_product(product_name)
        raise HTTPException(404, "Product not found")

    @staticmethod
    def delete_product(product_name: str) -> Product:
        if product_name in _product:
            product = ProductInterface.get_product(product_name)
            del _product[product_name]
            return product
        raise HTTPException(404, "Product not found")
