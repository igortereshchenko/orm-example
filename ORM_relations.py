from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from database_connection import  engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Customers(Base):

    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    address = Column(String(30))
    email = Column(String(30))

    invoices = relationship("Invoice", back_populates='customers')



class Invoice(Base):

    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    custid = Column(Integer, ForeignKey('customers.id'))
    amount = Column(Integer)

    customers = relationship("Customers", back_populates = "invoices")



Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


rows = [

    Customers(
        id=1,
        name='Bob',
        address='Kyiv',
        email='bob@gmail.com',
        invoices= [
                    Invoice(id=1, amount=9),Invoice(id=2, amount=19)
                  ]
    ),

    Customers(
        id=2,
        name='Boba',
        address='Kyiv',
        email='boba@gmail.com',
        invoices=[
            Invoice(id=3, amount=19), Invoice(id=4, amount=19), Invoice(id=5, amount=191)
        ]
    ),

]

# session.add_all(rows)
# session.commit()

# TIMES
for customer, invoice in session.query(Customers,Invoice).filter(Customers.id==Invoice.custid).all():
    print(customer.id, customer.name, invoice.amount)

#    JOIN
for customer in session.query(Customers).join(Invoice).all():
    print(customer.name )
    for invoice in customer.invoices:
        print(invoice.amount)


# customer name , count(invoice)

"""
    select c.name, count(invoice.id) invoice_count
    from custome c NATURAL JOIN invoice
    group by c.id, c.name
"""
# HOMEWORK implement

from sqlalchemy.sql import func


"""
    select custid, count(*) invoice_count
    from invoice
    group by custid
"""
sub_query = session.query(Invoice.custid, func.count('*').label('invoice_count')).group_by(Invoice.custid).subquery() #view = OBJECT = TABLE

"""
    select customer.name, sub_query.invoice_count
    from
        customers join (
        
                             select custid, count(*) invoice_count
                                from invoice
                                group by custid
                        ) sub_query
        on   customers.id =  sub_query.custid
"""

for customer, cuts_id_table,  invoice_count_table in session.query(Customers, sub_query).outerjoin(sub_query, Customers.id ==sub_query.c.custid).order_by(Customers.id):
    print(customer.name, cuts_id_table,  invoice_count_table)





