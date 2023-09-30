from sqlalchemy import (
    Column, Integer, Boolean, String, ForeignKey, Float
)
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from api.database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(
        Integer, primary_key=True, nullable=False, unique=True
        )
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    control = Column(String, nullable=False, server_default='user')
    created_at = Column(
        TIMESTAMP, server_default=text('now()'), nullable=False
    )


class Products(Base):
    __tablename__ = "products"

    id = Column(
        Integer, primary_key=True, nullable=False, unique=True
        )
    name = Column(String, nullable=False)
    barcode = Column(
        String, nullable=False,unique=True
        )
    brand = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    available = Column(Boolean, nullable=False, server_default="True")
    created_at = Column(
        TIMESTAMP, server_default=text('now()'), nullable=False
    )
    admin_name = Column(Integer, ForeignKey(
        column="users.username", ondelete="SET NULL"
         , server_default="default-admin"), nullable=False
    )

class Reviews(Base):
    __tablename__ = "product_reviews"

    username = Column(
        String, ForeignKey(column="users.username")
        , ondelete="CASCADE")
    product_id = Column(
        String, ForeignKey(column="products.barcode")
        , ondelete="CASCADE")
    user_review = Column(String, nullable=False)
    user_rating = Column(Integer, nullable=False)
    created_at = Column(
        TIMESTAMP, server_default=text('now()'), nullable=False
    )
    user_info = relationship("Users")
    posts_info = relationship("Products")


