from fastapi import APIRouter, Depends, HTTPException
from interfaces import ProductInterface
from typing import List
from models.product import Product, ProductNameless
from fastapi.params import Body, Path
from sqlalchemy.orm.session import Session
from database import get_db


router = APIRouter(prefix="/product")


@router.post("/", response_model=Product, tags=["product"])
async def create_product(
    product_creation: Product = Body(
        ...,
        example={
            "name": "Beterraba",
            "description": "A mais nova beterraba usada para cozinhar",
            "price": 3.75,
        },
    ),
    db: Session = Depends(get_db),
):  
    product_exists = ProductInterface.get_product(db, product_creation.name) is not None
    if product_exists:
        raise HTTPException(400, "Product already exists")

    product = ProductInterface.create_product(db, product_creation)
    return product


@router.get("/", response_model=List[Product])
async def get_products(db: Session = Depends(get_db)):
    products = ProductInterface.get_products(db)
    return products


@router.patch("/{name}", response_model=Product)
async def update_product(
    name: str = Path(..., example="Batata"),
    product_update: ProductNameless = Body(
        ...,
        example={
            "description": "A mais nova batata usada para cozinhar, a batata do milenio",
            "price": 3.75,
        },
    ),
    db: Session = Depends(get_db),
):
    product = ProductInterface.update_product(db, name, product_update)
    return product


@router.get("/{name}", response_model=Product)
async def get_product(
    name: str = Path(..., example="Batata"), db: Session = Depends(get_db)
):
    product = ProductInterface.get_product(db, name)
    return product


@router.delete("/{name}", response_model=Product)
async def delete_product(
    name: str = Path(..., example="Batata"), db: Session = Depends(get_db)
):
    product = ProductInterface.delete_product(db, name)
    return product
