from typing import List, Optional

import schemas
from models.product import Product
from sqlalchemy.orm import Session


class ProductInterface:
    @staticmethod
    def get_products(db: Session) -> List[Product]:
        return db.query(schemas.Product).all()

    @staticmethod
    def get_product(db: Session, product_name: str) -> Optional[Product]:
        return db.query(schemas.Product).filter(schemas.Product.name == product_name).first()

    @staticmethod
    def create_product(db: Session, product: Product) -> Product:
        product = schemas.Product(**product.dict())
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def update_product(db: Session, product_name: str, product_update: Product) -> Optional[Product]:
        db.query(schemas.Product).filter(schemas.Product.name == product_name).update(
            product_update.dict(), synchronize_session="fetch")
        db.commit()
        return ProductInterface.get_product(db, product_name)

    @staticmethod
    def delete_product(db: Session, product_name: str) -> Optional[Product]:
        product = db.query(schemas.Product).filter(schemas.Product.name == product_name).first()
        db.delete(product)
        db.commit()
