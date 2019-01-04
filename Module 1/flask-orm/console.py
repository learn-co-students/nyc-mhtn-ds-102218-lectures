import sqlalchemy
from sqlalchemy.orm import sessionmaker

# codebase
from listing import Base, Listing
from scrape_craigslist import ListingBuilder, CraigsListScraper, ListingParser

# database
engine = sqlalchemy.create_engine('sqlite:///craigslist.db', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
