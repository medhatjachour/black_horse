from typing import List, Union
from datetime import datetime ,date
import pydantic as _pydantic

class Product(_pydantic.BaseModel):
    id:str
    name:str
    file_path:str
    color_id:int
    size_id:int
    num:int
    price_in:int
    price_out:int
    class Config:
        orm_mode = True

class Size(_pydantic.BaseModel):
    id:str
    size: str
    class Config:
        orm_mode = True

class Color(_pydantic.BaseModel):
    id:str
    color: str
    class Config:
        orm_mode = True

class User(_pydantic.BaseModel):
    id:int
    name: str
    password: str
    user_type: bool
    class Config:
        orm_mode = True

class OutPut(_pydantic.BaseModel):
    id: int
    num: int
    disc: str
    date: Union[datetime, None] = None
    class Config:
        orm_mode = True

class Sales(_pydantic.BaseModel):
    id:int
    name: Union[str, None] = None
    phone: Union[str, None] = None
    link: Union[str, None] = None
    date: Union[datetime, None] = None
    total: int
    status: Union[str, None] = None
    real_total: Union[int, None] = None
    class Config:
        orm_mode = True

class Sale_item(_pydantic.BaseModel):
    id:int
    sale_id: int
    product_id: int
    num_of_products: int
    price_out: int
    class Config:
        orm_mode = True
