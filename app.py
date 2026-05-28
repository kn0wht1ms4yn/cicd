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

app.run(host='0.0.0.0', port=9000, debug=True)
