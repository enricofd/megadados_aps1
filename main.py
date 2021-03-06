from fastapi import FastAPIs
from routes import cart, product
from database import Base, engine

description = """
Uma API de carrinho de compras. A melhor API de
compras da história das compras. Venha comprar.

## Produtos
Você poderá:
* **Criar produtos**
* **Consultar produtos**
* **Editar produtos**
* **Deletar produtos**

## Carrinhos
Você poderá:
* **Criar carrinhos**
* **Consultar carrinhos**
* **Editar carrinhos**
* **Deletar carrinhos**

"""

tags_metadata = [
    {
        "name": "product",
        "description": "Operações com produtos. Você pode **criar**, **atualizar**, **deletar** e **consultar** itens",
    },
    {
        "name": "cart",
        "description": "Operações com carrinhos. Você pode **criar**, **atualizar**, **deletar** e **consultar** carrinhos",
    },
]

app = FastAPI(
    title="MegadadosAPI",
    description=description,
    version="0.0.1",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.get("/")
async def root():
    return {"app": "megadados"}


app.include_router(product.router)
app.include_router(cart.router)

Base.metadata.create_all(bind=engine)
