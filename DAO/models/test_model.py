from sqlalchemy import Table, Integer, String, Column, MetaData


# BigInteger
# Boolean
# Date
# DateTime
# Float
# Integer
# Numeric
# SmallInteger
# String
# Text
# Time
meta = MetaData()

students = Table(
    'students',
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('lastname', String(30)),

)

books = Table(
    'books',
    meta,
    Column('id', Integer, primary_key=True),
    Column('book_name', String(30))

)