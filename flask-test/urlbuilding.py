
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
  url_for('index')
  url_for('login')
  url_for('login', next='/')
  url_for('profile', username='John Doe')
