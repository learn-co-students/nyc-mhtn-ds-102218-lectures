from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dash

server = Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///craigslist.db'
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
server.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(server)

app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/')

from dash_package.scrape_craigslist import ListingBuilder, CraigsListScraper, ListingParser

from dash_package.models import *
from dash_package.routes import *
from dash_package.dashboard import *
