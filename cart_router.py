from fastapi import APIRouter

router = APIRouter(prefix='/cart')


# /cart
# - POST: criar
@router.post("")
async def create_cart():
    return {"POST": "CREATE_CART"}

# - GET: listar carrinhos

# /cart/:id_cart/
# - GET: listar produtos em um cart
# - POST: adicionar item x quantidade
# - DELETE: deletar cart (itens também)

# /cart/:id_cart/:id_item
# - DELETE: remover item
# - PATCH: editar quantidade
