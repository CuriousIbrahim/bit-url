from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func, text
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.dialects.postgresql import INET

import csv

from config import NAME, PASSWORD, DB_NAME, HOST

# try:
#     conn = psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}'"
#                             .format(DB_NAME, NAME, 'localhost', PASSWORD))
# except:
#     print("Unable to connect to database")
#
#
# cur = conn.cursor()
#
# with open('create.sql') as f:
#     data = f.read()
#     cur.execute(data)
#     # cur.commit()
#     conn.commit()



Base = declarative_base()

url = 'postgresql://{}:{}@{}/{}'.format(NAME, PASSWORD, HOST, DB_NAME)

print('new db url', url)

engine = create_engine(url, echo=True)


# class User(Base):
#     __tablename__ = "user"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     first_name = Column(String)
#     last_name = Column(String)


class Url(Base):
    __tablename__ = "url"

    id = Column(String, primary_key=True)
    original_url = Column(String)
    times_visited = Column(Integer, server_default=text("0"))
    timestamp_added = Column(DateTime, server_default=func.now())

    visit = relationship("Visit")


class IpAddress(Base):
    __tablename__ = 'ip_address'

    # id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(INET, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    # # hostname = Column(String)
    # # zipcode = Column(String)
    # # latitude = Column(Float)
    # # longitude = Column(Float)
    # # timezone = Column(String, ForeignKey("timezone.name"))
    # # country_id = Column(Integer)
    # # city_name = Column(String)
    # # region = Column(String)
    #
    # visit = relationship("Visit")
    #
    # ForeignKeyConstraint(['country_id', 'city.country_id'], ['city', 'city.name'])



class Visit(Base):
    __tablename__ = "visit"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(INET, ForeignKey('ip_address.ip'))
    url = Column(String, ForeignKey("url.id"))
    visited_at = Column(DateTime)


class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, autoincrement=True, primary_key=True)
    code = Column(String)
    name = Column(String)
    iso_code = Column(String)
    iso_code_2 = Column(String)

    city = relationship('City')


class City(Base):
    __tablename__ = "city"

    name = Column(String, primary_key=True)
    country_id = Column(Integer, ForeignKey("country.id"), primary_key=True)

    # ip_address = relationship("IpAddress")


class Timezone(Base):
    __tablename__ = "timezone"

    name = Column(String, primary_key=True)

    # ip_address = relationship("IpAddress")



def create():
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    with open('countries.csv') as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            obj = Country(code=row[1], name=row[0], iso_code=row[2], iso_code_2=row[3])
            session.add(obj)

    session.commit()

create()