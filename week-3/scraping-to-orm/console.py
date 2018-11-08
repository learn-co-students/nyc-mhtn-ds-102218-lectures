from listing import Listing
from scrape_craigslist import ListingParser, ListingBuilder, CraigsListScraper
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///craigslist.db', echo=True)
from listing import Base

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
