from flask import Flask, request
import pdb
app = Flask(__name__)


@app.route('/jobs')
def get_jobs():
    return '<ul> <li> Hello jobs</li> <li> World! <\li> </ul> '

if __name__ == 'main':
    app.run(debug = True)
