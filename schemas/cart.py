from database import Base
from sqlalchemy import Column, Integer


class Cart(Base):
    __tablename__ = "cart"

    id_cart = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, nullable=False, default=1)
