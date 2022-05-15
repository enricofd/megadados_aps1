from database import Base
from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship



class Cart(Base):
    __tablename__ = "cart"

    cart_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, nullable=False, default=1)

    cart_product = relationship("CartProduct", cascade="all, delete-orphan")
