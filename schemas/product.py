from sqlalchemy import Column, String, Float
from database import Base


class Product(Base):
    __tablename__ = "product"

    name = Column(String(45), primary_key=True, index=True)
    description = Column(String(100), nullable=False)
    price = Column(Float(2), nullable=False)
