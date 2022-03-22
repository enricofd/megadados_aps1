from doctest import Example
from fastapi import APIRouter
from interfaces import ProductInterface
from typing import List
from models.product import Product, ProductNameless
from fastapi.params import Body, Path



router = APIRouter(prefix="/product")

@router.post("/", response_model=Product, tags=["product"])
async def create_product(product_creation: Product = Body(..., example = {
	"name": "Beterraba",
	"description": "A mais nova beterraba usada para cozinhar",
	"price": 3.75
})):
    product = ProductInterface.create_product(product_creation)
    return product

@router.get("/", response_model=List[Product])
async def get_products():
    products = ProductInterface.get_products()
    return products

@router.patch("/{name}", response_model=Product)
async def update_product(name: str= Path(..., example="Batata"), product_update: ProductNameless = Body(...,example={
	"description": "A mais nova batata usada para cozinhar, a batata do milenio",
	"price": 3.75
})):
    product = ProductInterface.update_product(name, product_update)
    return product

@router.get("/{name}", response_model=Product)
async def get_product(name: str = Path(..., example="Batata")):
    product = ProductInterface.get_product(name)
    return product

@router.delete("/{name}", response_model=Product)
async def delete_product(name: str = Path(..., example="Batata")):
    product = ProductInterface.delete_product(name)
    return product
