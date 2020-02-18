from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func, text

from config import NAME, PASSWORD, DB_NAME

Base = declarative_base()

url = 'postgresql://{}:{}@localhost/{}'.format(NAME, PASSWORD, DB_NAME)

engine = create_engine(url, echo=True)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)


class Url(Base):
    __tablename__ = "urls"

    id = Column(String, primary_key=True)
    original_url = Column(String)
    times_visited = Column(Integer, server_default=text("1"))
    timestamp_added = Column(DateTime, server_default=func.now())
    disabled_on = Column(DateTime)

# Base.metadata.create_all(engine)


