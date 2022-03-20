from fastapi import FastAPI
from cart_router import router as cart_router
from product_router import router as product_router


app = FastAPI()


@app.get('/')
async def root():
    return {"app": "megadados"}


app.include_router(product_router)
app.include_router(cart_router)
