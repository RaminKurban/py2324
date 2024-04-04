from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey, CheckConstraint, Boolean, DateTime, MetaData
from datetime import datetime


metadata = MetaData()

telsprav = Table('telsprav', metadata,
                 Column('id', Integer(), primary_key=True),
                 Column('name', String(50), nullable=False, index=True),
                 Column('surname', String(50), nullable=True, index=True),
                 Column('phone', String(20), nullable=False),
                 Column('about', Text(), nullable=True),

                 Column('address',String(200),nullable=True)
                 )

ed = Table('extradata',metadata,
           Column('id',Integer(),primary_key=True),
           Column('client_id',Integer,ForeignKey('telsprav.id')),
           Column('age',Integer,nullable=False),
           Column('heigest',Integer,nullable=True),
           Column('country',String(50),nullable=False),
           Column('City',String(50),nullable=False),
           Column('businessman',Boolean, default=False),
           Column('created',DateTime,default=datetime.now),
           CheckConstraint('age > 18',name='age_check')
           )
