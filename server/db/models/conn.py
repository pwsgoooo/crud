from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from typing import Text
from .base import Base
import mysql.connector
from .members import Members
from core.setting import settings

host = 'localhost'
dbname = 'board'
port = 3306
user = 'test'
pw = 'Testtest12'

DATABASE = settings.DATABASE_URL

ENGINE =  create_engine(DATABASE,echo=True)

SESSON = scoped_session(sessionmaker(autoflush=False, autocommit=False,bind=ENGINE))

Base.query = SESSON.query_property()


fconn = mysql.connector.connect(
    host=host,
    database = dbname,
    user = user,
    password = pw
)

CURSOR = fconn.cursor()

tablename = [Members.__tablename__]

# for t_name in tablename:
#     namet = t_name

#     q1 = 'DROP TABLE IF EXIST {namet};'

#     def start_ctable():
#         for i in tablename:
#             CURSOR.execute(q1)

def create_tables():    
    Base.metadata.create_all(bind=ENGINE)

