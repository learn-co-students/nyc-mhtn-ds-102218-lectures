from flask import Flask, render_template
from console import session
from listing import Listing
import pdb
# class Flask()

app = Flask(__name__)

@app.route('/apartments')
def render_apartments():
    apartment = session.query(Listing).first()
    return apartment.title
    # return render_template('index.html', apartments = apartments)

if __name__ == '__main__':
    app.run(debug = True)
