from fastapi import APIRouter

from models.product import Product, ProductCreation


router = APIRouter(prefix='/product')

# /product

# POST: criar produto


@router.post("", response_model=Product)
async def create_product(product: ProductCreation):
    product = Product(product_id=1, **product.dict())
    product.product_id = 123
    return product

# GET: listar produtos

# /product/:product_id
# PUT: atualizar produto
# GET: listar produto
# DELETE: remover produto
# PATCH: atualizar informações de um produto
