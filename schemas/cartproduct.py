from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base


class CartProduct(Base):
    __tablename__ = "cart_product"

    id_cart = Column(Integer, ForeignKey("cart.cart_id"), primary_key=True, index=True)
    name = Column(String(45), ForeignKey("product.name"), primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
