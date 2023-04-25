from passlib.hash import bcrypt
import datetime as _dt

from orm import database as _database 
import sqlalchemy.orm as _orm
from orm import models as _models
from orm import schemas as _schemas
# authenticheckion
import os
from os.path import isdir, isfile, join

# https://www.youtube.com/watch?v=6hTRw_HK3Ts
def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def authenticate_user(user_name: str, password: str, db: _orm.Session):
    user = db.query(_models.Staff).filter(_models.Staff.user_name == user_name).first()
    if not user :
        return False
    if not bcrypt.verify(password ,user.hash_password):
        return False
    return user 
    
#Product
def get_product_by_name(db: _orm.Session , name:str):
    return db.query(_models.Product).filter(_models.Product.name == name).first()
def get_products_by_name(db: _orm.Session , name:str):
    return db.query(_models.Product).filter(_models.Product.name == name).all()
# Users
def get_user_by_userName(db: _orm.Session , name:str):
    return db.query(_models.User).filter(_models.User.name == name).first()


#  product ################################################

def create_Product(db: _orm.Session, product: _schemas.Product):
    product = _models.Product(**product)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_products(db: _orm.Session):
    return db.query(_models.Product).all()

def get_products_count(db: _orm.Session):
    return db.query(_models.Product).count()

def get_products_pages(db: _orm.Session, skip:int, limit:int):
    # return db.query(_models.Product).offset(skip).limit(limit).all()
    return db.query(_models.Product).offset(skip).limit(limit).all()
    # users.select().order_by(users.c.id.desc()).limit(5)
    # return db.query(_models.Product).all()[-limit]

def get_product_by_id(db: _orm.Session, id: str):
    return db.query(_models.Product).filter(_models.Product.id == id).first()

def get_products_by_name(db: _orm.Session, name: str):
    return db.query(_models.Product).filter(_models.Product.name == name).all()

def get_products_by_name_and_size(db: _orm.Session, name: str, size: str):
    return db.query(_models.Product).filter(_models.Product.name == name).filter(_models.Product.size == size).all()

def get_products_by_name_and_color(db: _orm.Session, name: str, color: str):
    return db.query(_models.Product).filter(_models.Product.name == name).filter(_models.Product.color == color).all()

def get_product(db: _orm.Session, name: str, color: str, size: str):

    return db.query(_models.Product).filter(_models.Product.name == name ).filter(_models.Product.size == size).filter(_models.Product.color == color ).first()

def delete_product(db: _orm.Session, product_id:str):
    db.query(_models.Product).filter(_models.Product.id  == product_id).delete()
    db.commit()

def update_product(db: _orm.Session, product_id:str, num:str, price_in:str, price_out:str, file_path:str):
    db_product = get_product_by_id(db = db ,id =  product_id)

    # db_product.name = product.name
    # db_product.color_id = product.middle_name
    # db_product.size_id = product.size_id
    db_product.num = num
    db_product.price_in = price_in
    db_product.price_out = price_out
    db_product.file_path = file_path
    # db_product.price_in = product.price_in
    # db_product.price_out = product.price_out

    db.commit()
    db.refresh(db_product)
    return db_product

def update_product_num(db: _orm.Session, product_id:str, num:str):
    db_product = get_product_by_id(db = db ,id =  product_id)

    # db_product.name = product.name
    # db_product.color_id = product.middle_name
    # db_product.size_id = product.size_id
    db_product.num = int(db_product.num) - int(num)
    # db_product.price_in = product.price_in
    # db_product.price_out = product.price_out

    db.commit()
    db.refresh(db_product)
    return db_product


def update_refused_product_num(db: _orm.Session, product_id:str, num:str):
    db_product = get_product_by_id(db = db ,id =  product_id)

    # db_product.name = product.name
    # db_product.color_id = product.middle_name
    # db_product.size_id = product.size_id
    db_product.num = int(db_product.num) + int(num)
    # db_product.price_in = product.price_in
    # db_product.price_out = product.price_out

    db.commit()
    db.refresh(db_product)
    return db_product


#  Size ################################################

def create_size(db: _orm.Session , size:_schemas.Size ):
    size = _models.Size(**size)
    db.add(size)
    db.commit()
    db.refresh(size)
    return size

def get_size(db: _orm.Session, name: str):
    return db.query(_models.Size).filter(_models.Size.name == name).first()

def get_sizes(db: _orm.Session):
    return db.query(_models.Size).all()

def delete_size(db: _orm.Session, size_id:str):
    db.query(_models.Size).filter(_models.Size.id  == size_id).delete()
    db.commit()

#  Color ################################################

def create_color(db: _orm.Session , color:_schemas.Color ):
    color = _models.Color(**color)
    db.add(color)
    db.commit()
    db.refresh(color)
    return color

def get_color(db: _orm.Session, name: str):
    return db.query(_models.Color).filter(_models.Color.name == name).first()

def get_colors(db: _orm.Session):
    return db.query(_models.Color).all()

def delete_color(db: _orm.Session, color_id:str):
    db.query(_models.Color).filter(_models.Color.id  == color_id).delete()
    db.commit()

#  User ################################################

def create_user(db: _orm.Session , user:_schemas.User ):
    user = _models.User(**user)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: _orm.Session, name: str):
    return db.query(_models.User).filter(_models.User.name == name).first()

def get_users(db: _orm.Session):
    return db.query(_models.User).all()

def delete_user(db: _orm.Session, user_id:int):
    db.query(_models.User).filter(_models.User.id  == user_id).delete()
    db.commit()
#  User ################################################

def create_output(db: _orm.Session , output:_schemas.OutPut ):
    output = _models.OutPut(**output)
    db.add(output)
    db.commit()
    db.refresh(output)
    return output

# def get_output(db: _orm.Session, name: str):
#     return db.query(_models.User).filter(_models.User.name == name).first()

def get_outputs(db: _orm.Session):
    return db.query(_models.OutPut).all()
#  Sales ################################################

def create_sales(db: _orm.Session , sales:_schemas.Sales ):
    sales = _models.Sales(**sales)
    db.add(sales)
    db.commit()
    db.refresh(sales)
    return sales

def get_sales(db: _orm.Session, sales_id: int):
    return db.query(_models.Sales).filter(_models.Sales.id == sales_id).first()

def get_sales_by_id(db: _orm.Session, sales_id: int):
    return db.query(_models.Sales).filter(_models.Sales.id == sales_id).all()

def get_sales_by_name(db: _orm.Session, name: str):
    return db.query(_models.Sales).filter(_models.Sales.name == name).all()

def get_sales_by_phone(db: _orm.Session, phone: str):
    return db.query(_models.Sales).filter(_models.Sales.phone == phone).all()

def get_sales_by_status(db: _orm.Session, status: str):
    return db.query(_models.Sales).filter(_models.Sales.status == status).all()

def get_sales_by_link(db: _orm.Session, link: str):
    return db.query(_models.Sales).filter(_models.Sales.link == link).all()


def get_all_sales(db: _orm.Session):
    return db.query(_models.Sales).all()

def delete_sale(db: _orm.Session, sales_id:int):
    db.query(_models.Sales).filter(_models.Sales.id  == sales_id).delete()
    db.commit()


def change_sale_status(db: _orm.Session, sales_id:int, status:str):
    db_record = get_sales(db = db , sales_id = sales_id )
    db_record.status = status
    db.commit()
    db.refresh(db_record)
    return db_record


def finish_sale(db: _orm.Session, sales_id:int, total:str, real_total:str):
    db_record = get_sales(db = db , sales_id = sales_id )
    db_record.total = total
    db_record.real_total = real_total
    db.commit()
    db.refresh(db_record)
    return db_record



#  Sales items ################################################

def create_Sale_item(db: _orm.Session , Sale_item:_schemas.Sale_item ):
    Sale_item = _models.Sale_item(**Sale_item)
    db.add(Sale_item)
    db.commit()
    db.refresh(Sale_item)
    return Sale_item

def get_sale(db: _orm.Session, Sale_item_id: int):
    return db.query(_models.Sale_item).filter(_models.Sale_item.id == Sale_item_id).first()

def get_sales_items(db: _orm.Session, sale_id: int):
    return db.query(_models.Sale_item).filter(_models.Sale_item.sale_id == sale_id).all()

def delete_sale(db: _orm.Session, Sale_item_id:int):
    db.query(_models.Sale_item).filter(_models.Sale_itemale_item.id  == Sale_item_id).delete()
    db.commit()



# stores ###################################################


def create_store(db: _orm.Session , store:_schemas.Store ):
    store = _models.Store(**store)
    db.add(store)
    db.commit()
    db.refresh(store)
    return store

def get_store(db: _orm.Session, name: str):
    return db.query(_models.Store).filter(_models.Store.name == name).first()

def get_stores(db: _orm.Session):
    return db.query(_models.Store).all()

def delete_store(db: _orm.Session, store_id:str):
    db.query(_models.Store).filter(_models.Store.id  == store_id).delete()
    db.commit()

# Cat ###################################################
def create_cat(db: _orm.Session , cat:_schemas.Cat ):
    cat = _models.Cat(**cat)
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat

def get_cat(db: _orm.Session, name: str):
    return db.query(_models.Cat).filter(_models.Cat.name == name).first()

def get_cats(db: _orm.Session):
    return db.query(_models.Cat).all()

def delete_cat(db: _orm.Session, cat_id:str):
    db.query(_models.Cat).filter(_models.Cat.id  == cat_id).delete()
    db.commit()

# Checks ###################################################
def create_check(db: _orm.Session , check:_schemas.Check ):
    check = _models.Check(**check)
    db.add(check)
    db.commit()
    db.refresh(check)
    return check

def get_check(db: _orm.Session, name: str):
    return db.query(_models.Check).filter(_models.Check.name == name).first()

def get_checks(db: _orm.Session):
    return db.query(_models.Check).all()

def delete_check(db: _orm.Session, check_id:str):
    db.query(_models.Check).filter(_models.Check.id  == check_id).delete()
    db.commit()


    # Checks items ###################################################

def create_check_item(db: _orm.Session , check_item:_schemas.Check_item ):
    check_item = _models.Check_item(**check_item)
    db.add(check_item)
    db.commit()
    db.refresh(check_item)
    return check_item

def get_check_item(db: _orm.Session, id: int):
    return db.query(_models.Check_item).filter(_models.Check_item.id == id).first()

def get_check_items(db: _orm.Session, check_id: int):
    return db.query(_models.Check_item).filter(_models.Check_item.check_id == check_id).all()

def get_all_check_items(db: _orm.Session):
    return db.query(_models.check_item).all()

def delete_check_item(db: _orm.Session, check_item_id:int):
    db.query(_models.Check_item).filter(_models.Check_item.id  == check_item_id).delete()
    db.commit()

