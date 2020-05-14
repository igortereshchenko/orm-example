from database_connection import engine
from DAO.models.table_relations import students, meta, addresses
from sqlalchemy.sql import select
from sqlalchemy import and_, or_, between, asc, desc


meta.create_all(engine)

connection =engine.connect()

# connection.execute(
#
#     students.insert(),[
#                         {'id':1,'name':'Bob','lastname':'Bobovitch'},
#                         {'id':2,'name':'Boba','lastname':'Bobovitch'}
#                        ]
#
#
# )
#
# connection.execute(
#
#     addresses.insert(), [
#                             {'id': 1, 'st_id': 1,'email':'bob@gmail.com','zip':'001'},
#                             {'id': 2, 'st_id': 1,'email':'bob@ukr.net','zip':'001'},
#                             {'id': 3, 'st_id': 2, 'email': 'boba@gmail.com', 'zip': '002'},
#                             {'id': 4, 'st_id': 2, 'email': 'boba@ukr.net', 'zip': '002'},
#                             {'id': 5, 'st_id': 2, 'email': 'boba@i.ua', 'zip': '002'},
#
#                          ]
#
# )


# TIMES + WHERE
select_query = select([students, addresses]).where(students.c.id == addresses.c.st_id)  # select_query = students.select()
print(select_query)

result = connection.execute(select_query)
for row in result:
    print(row)

#  JOIN
join_query = students.join(addresses,students.c.id == addresses.c.st_id) # create view on this PC
select_query = select([students.c.name, addresses.c.zip, addresses.c.email]).select_from(join_query) # get data from view


result = connection.execute(select_query)
for row in result:
    print(row)

# and or between ....
# find student with (lastname = Bobovitch and id>1 ) or name=='Bob'
search_query = select([students]).where( or_(  and_( students.c.lastname=='Bobovitch', students.c.id>1  ), students.c.name=='Bob'  ))
result = connection.execute(search_query)
for row in result:
    print(row)


# asc desc
search_query = select([students]).order_by(asc(students.c.name)).where( or_(  and_( students.c.lastname=='Bobovitch', students.c.id>1  ), students.c.name=='Bob'  ))
result = connection.execute(search_query)
for row in result:
    print(row)

# between
search_query = select([students]).where(between(students.c.id,2,4))
result = connection.execute(search_query)
for row in result:
    print(row)


