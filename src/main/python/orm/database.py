import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import os
from os.path import isdir, join

db_folder = join(os.getenv('USERPROFILE'), 'gm3a-data')
if not isdir(db_folder):
    os.mkdir(db_folder)
    
SQLALCHEMY_DATABASE_URL = "sqlite:///" + join(db_folder, 'database.db')
engine = _sql.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False,}, pool_size=200, max_overflow=-1
)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = _declarative.declarative_base()