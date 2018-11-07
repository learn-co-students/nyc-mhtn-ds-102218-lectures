from apartment import Apartment
from craigslist import CraigsList
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///craigslist.db', echo=True)
from listing import Base

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
