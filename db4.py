from sqlalchemy import create_engine,  insert
from table_structure import metadata,telsprav,ed
from datetime import datetime
import table_structure
#CheckConstraint - проверка данных (сравнение)
#Boolean -проверка Да или Нет (true или false)

#sqlalchemy вязь между программой и базой данных (автоматизировванная)
#psycopg2 расширенная связь с базой

#engine = create_engine("mysql+pymysql://alch:123456@10.10.101.193:3306/mydb")
engine = create_engine("postgresql+psycopg2://postgres:123456@10.10.101.193:5432/db4") # связь с базой данных
#postgresql (база данных)  куда подключаемся и psycopg2 это драйвер


connection = engine.connect()
metadata.create_all(engine)

# ins = telsprav.insert().values(
#     name = 'kirill',
#     surname = 'Morozov',
#     phone = '89214569874',
#     about = 'prepod',
#     address = 'Soyuz Sovetov',
#
#     )
# block_insert = insert(telsprav)
# result = connection.execute(block_insert, [
#     {
#     "name" : 'roman',
#     "surname" : 'Morozov',
#     "phone" : '89214569671',
#     "about" : 'prepod',
#     "address" : 'Gegmany',
#     },
#     {
#     "name" : 'Fedor',
#     "surname" : 'kalashnikov',
#     "phone" : '89214569675',
#     "about" : 'prepod',
#     "address" : 'Leninqrad',
#
#
#     }
#
# ])
#
# items = [
#     {
#         "name": 'Vladislav',
#         "surname": 'Drakula',
#         "phone": '5437363',
#         "about": 'vampir',
#         "address": 'Karpaty'
#     },
#     {
#         "name": 'Ivan',
#         "surname": 'Grozny',
#         "phone": '000000000',
#         "about": 'tcar',
#         "address": 'Horomy'
#     }
# ]
#
# result2 = connection.execute(block_insert, items)
#
#
# print(ins)
# print(ins.compile().params)
# execute_result = connection.execute(ins)
# print(execute_result)
# print(execute_result.inserted_primary_key)
# print(execute_result.is_insert)
# print(execute_result)

connection.commit()

print(engine)
ed_block_insert = insert(ed)
ed_items = [
    {
        "client_id":3,
        "age":1000,
        "heigest":200,
        "country":"Romania",
        "City":"Sigishoara",
        "businessman":True
        }
]
result3 = connection.execute(ed_block_insert, ed_items)
connection.commit()