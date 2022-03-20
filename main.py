from fastapi import FastAPI
from routes import cart_router, product_router

app = FastAPI()


@app.get('/')
async def root():
    return {"app": "megadados"}


app.include_router(product_router)
app.include_router(cart_router)
