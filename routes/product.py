from fastapi import APIRouter
from interfaces import ProductInterface
from typing import List
from models.product import Product, ProductNameless


router = APIRouter(prefix="/product")

# /product

# POST: criar produto
@router.post("/", response_model=Product)
async def create_product(product_creation: Product):
    product = ProductInterface.create_product(product_creation)
    return product


# GET: listar produtos
@router.get("/", response_model=List[Product])
async def get_products():
    products = ProductInterface.get_products()
    return products


# /product/:product_id

# PATCH: atualizar produto
@router.patch("/{name}", response_model=Product)
async def update_product(name: str, product_update: ProductNameless):
    product = ProductInterface.update_product(name, product_update)
    return product

# GET: listar produto
@router.get("/{name}", response_model=Product)
async def get_product(name: str):
    product = ProductInterface.get_product(name)
    return product

# DELETE: remover produto
@router.delete("/{name}", response_model=Product)
async def delete_product(name: str):
    product = ProductInterface.delete_product(name)
    return product