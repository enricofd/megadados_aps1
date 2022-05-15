import http
from models import cart
from models.product import Product
from models.cart import Cart, CartCreation, CartProduct
from fastapi import HTTPException
from typing import List

_product = {}
_cart = {}
_cartProduct = {}


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


class CartInterface:
    @staticmethod
    def get_id():
        try:
            id = max(list(_cart.keys())) + 1
            return id
        except:
            return 0

    @staticmethod
    def get_carts() -> List:
        return [Cart(**cart) for cart in _cart.values()]

    @staticmethod
    def get_cart(cart_id: int) -> Cart:
        try:
            return _cart[cart_id]
        except:
            raise HTTPException(400, "Cart does not exist")

    @staticmethod
    def create_cart(cart_creation: CartCreation):
        try:
            cart_id = CartInterface.get_id()
            _cart[cart_id] = {"cart_id": cart_id, **cart_creation.dict()}
            return _cart[cart_id]
        except:
            raise HTTPException(400, "Could not create cart")

    @staticmethod
    def delete_cart(cart_id: str) -> Cart:
        if cart_id in _cartProduct:
            del _cartProduct[cart_id]

        cart = CartInterface.get_cart(cart_id)
        del _cart[cart_id]
        return cart


class CartProductInterface:
    @staticmethod
    def get_cart_product(cart_id: int, product_name: str) -> CartProduct:
        if cart_id not in _cart:
            raise HTTPException(404, "Cart not found")

        if cart_id not in _cartProduct:
            raise HTTPException(404, "Cart is empty")

        if product_name not in _cartProduct[cart_id]:
            raise HTTPException(404, "Product not in cart")

        return CartProduct(**_cartProduct[cart_id][product_name])

    @staticmethod
    def get_cart_products(cart_id: int) -> List:
        if cart_id not in _cart:
            raise HTTPException(400, "Cart does not exist")

        if cart_id not in _cartProduct:
            return []

        return list(_cartProduct[cart_id].values())

    @staticmethod
    def add_to_cart(cart_id: int, cart_product: CartProduct) -> CartProduct:
        if cart_id not in _cart:
            raise HTTPException(400, "Cart does not exist")

        if cart_product.product_name not in _product:
            raise HTTPException(400, "Product does not exist")

        if cart_id not in _cartProduct:
            _cartProduct[cart_id] = {}

        if cart_product.product_name not in _cartProduct[cart_id]:
            _cartProduct[cart_id][cart_product.product_name] = cart_product.dict()
            return CartProductInterface.get_cart_products(cart_id)

        raise HTTPException(400, "Product already in cart")

    @staticmethod
    def update_quantity(cart_id: int, cart_update: CartProduct) -> List:
        if cart_id not in _cart:
            raise HTTPException(404, "Cart not found")

        if cart_id not in _cartProduct:
            raise HTTPException(404, "Cart is empty")

        product_name = cart_update.product_name

        if product_name not in _cartProduct[cart_id]:
            raise HTTPException(404, "Product not in cart")

        _cartProduct[cart_id][cart_update.product_name].update(
            {"quantity": cart_update.quantity}
        )

        return CartProductInterface.get_cart_product(cart_id, product_name)

    @staticmethod
    def remove_product(cart_id: int, product_name: str) -> CartProduct:
        try:
            product = _cartProduct[cart_id][product_name]
            del _cartProduct[cart_id][product_name]
            return product
        except:
            raise HTTPException(404, "Product is not in cart")
