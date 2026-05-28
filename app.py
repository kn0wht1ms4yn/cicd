'''
    Simple flask app demonstration.
'''
import subprocess
import flask
from flask import session
from db import db, insert_user, get_user

app = flask.Flask(__name__)
app.secret_key = 'Ohs3athibooteKutoo5quaeyahy4phaW'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db.init_app(app)
with app.app_context():
    db.create_all()
    users = [
        { 'username': 'admin', 'password': 'password' },
        { 'username': 'meow', 'password': 'meow123' },
        { 'username': 'bark', 'password': 'bark123' },
        { 'username': 'moo', 'password': 'moo123' },
        { 'username': 'oink', 'password': 'oink123' }
    ]
    for new_user in users:
        insert_user(new_user)

@app.get('/')
def index():
    '''
        index page
    '''
    session['index'] = True
    return ':)'

@app.get('/hi/<name>')
def route_hi(name):
    '''
        route /hi/<name>
    '''
    session['name'] = name
    tpl = f'Hello {name}!'
    return flask.render_template_string(tpl)

@app.get('/status/<port>')
def route_status(port):
    '''
        /status/<port>
    '''
    session['port'] = port
    cmd = f'netstat -tulnp | grep {port}'
    r = subprocess.check_output(cmd, shell=True)
    return r

@app.get('/user/<username>')
def route_user(username):
    '''
        route /user/<username>
    '''
    user = get_user(username)
    if user:
        return 'User found. :)'
    return 'User not found. :('

app.run(host='127.0.0.1', port=9000)
