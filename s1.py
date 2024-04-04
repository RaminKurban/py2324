from sqlalchemy import create_engine, asc, desc, select
from table_structure import telsprav,ed

# сортировки asc- прямая , desc -обратная

engine = create_engine("postgresql+psycopg2://postgres:123456@10.10.101.193:5432/db4")
connection = engine.connect()

# Выборка без фильтров
# sel1 = telsprav.select()
# print(sel1.compile())
# result = connection.execute(sel1)
# print(result.fetchall())


#sel1 = telsprav.select().where((telsprav.c.id < 100) & ((telsprav.c.name == "Ivan") | (telsprav.c.name == "Vladimir")))
#sel1 = telsprav.select().where(telsprav.c.surname.like('Morozov%')) # like -работает только с буквами
#sel1 = telsprav.select().where(telsprav.c.id.between(1,10)).order_by(desc(telsprav.c.id))
#sel1 = telsprav.select().where(telsprav.c.name.in_(["Ivan","Fedor","Vladimir"])) #in -все.
#sel1 = telsprav.select().where(telsprav.c.name.notin_(["Ivan","Fedor","Vladimir"]))# notin - кроме
#sel1 = telsprav.select().limit(3).offset(5) # offset- отступ, limit- сколько
sel1 = select(telsprav.c.name,telsprav.c.phone)

print(sel1.compile())
print(sel1.compile().params) # скомпелированный запрос с параметрами
result = connection.execute(sel1)
print(result.fetchall()) # все записи
#print(result.fetchone()) выбрать одну запись
#print(result.fetchmany(3))# выбор по 3 записи
print(result.rowcount)