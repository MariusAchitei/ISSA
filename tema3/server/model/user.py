from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# create table user(
# 	id bigint auto_increment primary key,
#     username varchar(255) not null,
#     is_owner bit not null
# password varchar(255) not null,
# );

class User(Base):
    __tablename__ = 'user'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    username = Column("username", String, nullable=False)
    is_owner = Column("is_owner", Boolean, nullable=False)
    password = Column("password", String, nullable=False)

    def __init__(self):
        self.id = None
        self.username = ''
        self.is_owner = 0
        self.password = ''
