from flask import render_template

from dash_package.models import Listing
import pdb
from dash_package import server
# class Flask()

@server.route('/apartments')
def render_apartments():
    apartment = Listing.query.get(1)
    return apartment.title
    # return render_template('index.html', apartments = apartments)
