'''
    Simple flask app demonstration.
'''
import flask

app = flask.Flask(__name__)

@app.get('/')
def index():
    '''
        index page
    '''
    return ':)'

app.run(host='127.0.0.1', port=9000)
