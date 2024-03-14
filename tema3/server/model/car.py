from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# create table cars(
# 	id bigint auto_increment primary key,
#     registered bit not null,
#     onlinee bit not null,
#     available bit not null,
#     owner_id bigint,
#     foreign key(owner_id) references user(id),
#     brand varchar(255),
#     model varchar(255),
# 	registration_number varchar(255) not null,
#     color varchar(255),
#     production_year int not null,
#     confort int
# )

class Car(Base):
    __tablename__ = 'cars'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    registered = Column("registered", bool, nullable=False)
    onlinee = Column("onlinee", bool, nullable=False)
    available = Column("available", bool, nullable=False)
    owner_id = Column("owner_id", Integer)
    brand = Column("brand", String)
    model = Column("model", String)
    registration_number = Column("registration_number", String, nullable=False)
    color = Column("color", String)
    production_year = Column("production_year", Integer, nullable=False)
    comfort = Column("comfort", Integer)

    """
    Constructor for a Series object. Takes as parameter the name of the series that is bound to become an instance of 
    the class
    """

    def __init__(self, name):
        self.id = None
        self.registered = 1
        self.onlinee = 1
        self.available = 1
        self.owner_id = None
        self.brand = ''
        self.model = ''
        self.registration_number = ''
        self.color = ''
        self.production_year = 0
        self.comfort = 0
