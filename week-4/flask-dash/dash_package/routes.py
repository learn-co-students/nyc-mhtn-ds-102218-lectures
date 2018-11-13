from flask import render_template
from dash_package.models import Listing
from dash_package import server
import pdb

@server.route('/apartments')
def render_apartments():
    listing = Listing.query.get(1)
    return 'apartment.title'
    # return render_template('index.html', apartments = apartments)
