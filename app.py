import flask
from flask import session

app = flask.Flask(__name__)

@app.get('/')
def index():
    return ':)'

app.run(host='0.0.0.0', port=9000, debug=True)