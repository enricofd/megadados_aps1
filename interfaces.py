from models import cart
from models.product import Product
from models.cart import Cart, CartCreation, CartProduct, CartProductNoID
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
    def get_carts() -> List:
        return [Cart(**cart) for cart in _cart.values()]

    @staticmethod
    def create_cart(cart_creation: CartCreation):
        try:
            cart_id = CartInterface.get_id()
            _cart[cart_id] = {"cart_id": cart_id, **cart_creation.dict()}
            return _cart[cart_id]
        except:
            raise HTTPException(400, "Could not create cart")
        
    @staticmethod
    def get_id():
        try:
            id = max(list(_cart.keys())) + 1
            return id
        except:
            return 0

    @staticmethod
    def update_cart(cart_id: str, cart_update: Cart) -> Cart:
        if cart_id in _cart:
            _cart[cart_id].update(cart_update.dict())
            return ProductInterface.get_cart(cart_id)
        raise HTTPException(404, "Cart not found")

    @staticmethod
    def delete_cart(cart_id: str) -> Product:
        if cart_id in _cart:
            cart = CartInterface.get_cart(cart_id)
            del _cart[cart_id]
            return cart
        raise HTTPException(404, "Cart not found")

class CartProductInterface:
    @staticmethod
    def get_cart_products(cart_id: int) -> List:
        try:
            products = list(_cartProduct[cart_id].values())
            return products
        except:
            raise HTTPException(404, "There are no products in your cart")

    @staticmethod
    def add_to_cart(cart_id: int, cart_product: CartProduct) -> CartProduct:
        if (cart_id not in _cartProduct):
            _cartProduct[cart_id] = {}
        if cart_product.product_name not in _cartProduct[cart_id]:
            _cartProduct[cart_id][cart_product.product_name] = cart_product.dict()
            return CartProductInterface.get_cart_products(cart_id)
        raise HTTPException(400, "Product already in cart")

    def update_cart_products(cart_id: int, cart_update: CartProduct) -> List:
        if cart_id in _cartProduct and cart_update.product_name in _cartProduct[cart_id]:
            _cartProduct[cart_id][cart_update.product_name].update(cart_update.dict())
            return CartProductInterface.get_cart_products(cart_id)
        raise HTTPException(404, "Cart not found")