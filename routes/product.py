from fastapi import APIRouter
from interfaces import ProductInterface
from typing import List
from models.product import Product


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
# PUT: atualizar produto
# GET: listar produto
# DELETE: remover produto
# PATCH: atualizar informações de um produto
