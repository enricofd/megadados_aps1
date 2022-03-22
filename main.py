from fastapi import FastAPI
from routes import cart_router, product_router

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
        "description": "Operações com produtos.",
    },
    {
        "name": "cart",
        "description": "Operações com carrinhos.",
    },
]

app = FastAPI(title="MegadadosAPI",
            description=description,
            version="0.0.1",
            license_info={
                "name": "Apache 2.0",
                "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
            })

@app.get('/')
async def root():
    return {"app": "megadados"}


app.include_router(product_router)
app.include_router(cart_router)
