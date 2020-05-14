from database_connection import engine
from DAO.models.test_model import students, meta, books

# create table
meta.create_all(engine)

# insert

# insert_query = "insert into ...." VS builder
insert_query = students.insert().values(id = 2, name = 'Boba', lastname = 'Bobovitch')
print(insert_query)

connection = engine.connect()
# connection.execute(insert_query)


# select

select_query = students.select()
print(select_query)
result = connection.execute(select_query)

for row in result:
    print(row)


# update
update_query = students.update().where( students.c.id==2 ).values(lastname = 'Bobovitch')
print(update_query)
connection.execute(update_query)


select_query = students.select()
print(select_query)
result = connection.execute(select_query)

for row in result:
    print(row)


# delete
delete_query = students.delete().where(students.c.lastname=='Bobovitch')
print(delete_query)
connection.execute(delete_query)

print(connection.execute(students.select()).fetchall())