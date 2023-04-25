import datetime as _dt

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship

from  orm.database import Base


class Product(Base):
    __tablename__ = "product"
    
    # min att
    id = Column(String, primary_key=True, index=True)

    name = Column(String)

    num = Column(String, nullable=True)

    file_path = Column(String, nullable=True)
    
    price_in = Column(String, nullable=True)
    price_out = Column(String, index=True, nullable=True)
    color = Column(String)
    size = Column(String)
    
    cat_id = Column(String, nullable=True)
    store_id = Column(String, nullable=True)
    check_id = Column(Integer, nullable=True)

class Size(Base):
    __tablename__ = "size"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique = True)
    
class Color(Base):
    __tablename__ = "color"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique = True)

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique = True)
    password = Column(String)
    user_type = Column(Boolean, default = False)

class OutPut(Base):
    __tablename__ = "output"
    id = Column(Integer, primary_key=True, index=True)
    num = Column(Integer)
    disc = Column(String)
    date = Column(DateTime, nullable=True)
class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=True)
    phone = Column(String, nullable=True)
    link = Column(String, nullable=True)
    date = Column(DateTime, nullable=True)
    total = Column(Integer)
    status = Column(String, nullable=True)
    real_total = Column(Integer, nullable=True)

    the_sale_items = relationship("Sale_item", back_populates="sale_items") 

class Sale_item(Base):
    __tablename__ = "sale_item"
    # we gonna need to modify that to match the schema
    id = Column(Integer, primary_key=True, index=True)

    num_of_products = Column(String, nullable = True)
    price_out = Column(String, nullable = True)

    sale_id = Column(Integer, ForeignKey("sales.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    
    sale_items = relationship("Sales",back_populates="the_sale_items")

class Check(Base):
    __tablename__ = "check"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=True)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)
    date = Column(DateTime, nullable=True)
    total = Column(Integer)
    paid = Column(Integer)

    the_check_items = relationship("Check_item", back_populates="check_items") 

class Check_item(Base):
    __tablename__ = "check_item"
    # we gonna need to modify that to match the schema
    id = Column(Integer, primary_key=True, index=True)

    date = Column(Date, nullable=True)
    paying =  Column(Integer)
    # status =  Column(Boolean)
    

    check_id = Column(Integer, ForeignKey("check.id"))    
    check_items = relationship("Check",back_populates="the_check_items")


class Store(Base):
    __tablename__ = "store"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique = True)
    phone = Column(String, nullable = True)
    address = Column(String, nullable = True)
   
class Cat(Base):
    __tablename__ = "cat"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique = True)

   