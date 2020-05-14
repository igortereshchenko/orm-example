from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from database_connection import  engine

Base = declarative_base()


class Customers(Base):

    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    address = Column(String(30))
    email = Column(String(30))
    comments = Column(String(30))



class GiftClass(Base):

    __tablename__ = 'gift'

    column1 = Column(String(20), primary_key=True)

Base.metadata.create_all(engine)