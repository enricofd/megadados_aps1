from fastapi import APIRouter
from dummy_db import ProductInterface

from models.product import Product


router = APIRouter(prefix='/product')

# /product

# POST: criar produto


# @router.post("", response_model=Product)
@router.post("/", response_model=Product)
async def create_product(product_creation: Product):
    product = ProductInterface.create_product(product_creation)
    return product

# GET: listar produtos

# /product/:product_id
# PUT: atualizar produto
# GET: listar produto
# DELETE: remover produto
# PATCH: atualizar informações de um produto
