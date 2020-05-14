from sqlalchemy import Table, Integer, String, Column, MetaData, ForeignKey


meta = MetaData()

students = Table(
    'students',
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('lastname', String(30)),

)

addresses = Table(
    'addresses',
    meta,
    Column('id', Integer, primary_key=True),
    Column('st_id', Integer, ForeignKey('students.id')),
    Column('zip', String(30)),
    Column('email', String(30))

)
