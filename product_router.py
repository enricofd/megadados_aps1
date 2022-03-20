from fastapi import APIRouter

router = APIRouter(prefix='/product')

# /product

# POST: criar produto
@router.post("")
async def create_product():
    return {"POST": "CREATE_PRODUCT"}
# GET: listar produtos

# /product/:product_id
# PUT: atualizar produto
# GET: listar produto
# DELETE: remover produto
# PATCH: atualizar informações de um produto
