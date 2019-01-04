from flask import Flask, request, render_template
import session
# import jobs_app
app = Flask(__name__)
import pdb
# get_apartments(neighborhood= 'brooklyn')
@app.route('/apartments/<neighborhood>')
def get_apartments(neighborhood):

    apartments = session.query(Apartment).first()
    return render_template('index.html', apartment = apartment)


if __name__ == '__main__':
    app.run(debug = True)
