from pimpmydb.columns import *
from pimpmydb.tables import Table
from pimpmydb.database import Database

id_column = IntColumn('id', primary_key=True)
print(id_column.get_sql_string())

name_column = VarcharColumn('name')
print(name_column.get_sql_string())

category_column = VarcharColumn('category')
print(category_column.get_sql_string())

description_column = TextColumn('description', null=True)
print(description_column.get_sql_string())

address_column = VarcharColumn('address', length=255, null=True)
print(address_column.get_sql_string())

email_column = VarcharColumn('email', length=255, null=True)
print(email_column.get_sql_string())

phone_column = VarcharColumn('phone', length=24, null=True)
print(phone_column.get_sql_string())

notes_column = TextColumn('notes', null=True)
print(notes_column.get_sql_string())

stores_table_columns = [id_column, name_column, category_column, description_column, address_column, email_column, notes_column]
stores_table = Table('stores', stores_table_columns)

db = Database()
db.create_table(stores_table)
