from database_connection import engine
from sqlalchemy.orm import sessionmaker

from DAO.models.Customers import Customers, GiftClass
from sqlalchemy import and_


Session = sessionmaker(bind=engine)

session = Session()


# insert = add
# customer = Customers(id =1, name='Bob', address='Kyiv', email='bob@gmail.com')
gift = GiftClass(column1='smth')

session.add(gift)
session.commit()

# session.add(customer)
#
# session.commit()
#
# # select * = all
# result = session.query(Customers).all()
#
# for row in result:
#     print(row.id, row.name)
#
#
# # where = filter
# result = session.query(Customers).filter( and_( Customers.id==1, Customers.email=='bob@gmail.com')  )
# for row in result:
#     print(row.id, row.name)
#
#
# # update
# session.query(Customers).filter(Customers.id==1).update(
#     {
#         Customers.name:"Mr."+Customers.name,
#         Customers.email:"no data"
#     },
#
#     synchronize_session = False
#
# )
#
# session.commit()
#
# result = session.query(Customers).all()
#
# for row in result:
#     print(row.id, row.name, row.email)
#
# # delete Homework

