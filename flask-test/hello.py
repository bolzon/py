
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'this is the index page'

@app.route('/hello')
def hello():
  return 'hello world!'

@app.route('/user/<username>')
def postuname(username):
  return 'user is "%s"' % username

@app.route('/id/<int:id>') # int, float, path
def postid(id):
  return 'id is: %d' % id

if __name__ == '__main__':
  app.run()
