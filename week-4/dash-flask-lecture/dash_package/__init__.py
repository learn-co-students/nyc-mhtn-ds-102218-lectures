# import sqlalchemy
# from sqlalchemy.orm import sessionmaker
import dash
# codebase
from flask import Flask
server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///craigslist.db'
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
server.config["SQLALCHEMY_ECHO"] = True

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(server)

app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/')




from dash_package.models import Listing

from dash_package.scrape_craigslist import ListingBuilder, CraigsListScraper, ListingParser

from dash_package.routes import *

from dash_package.dashboard import *

# database
# engine = sqlalchemy.create_engine('sqlite:///craigslist.db', echo=True)
#
# Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()
