
from flask import Flask
app = Flask(__name__)

@app.errohandler(404)
def not_found(error):
  return 'Sorry, I could not found the page you\'re searching for', 404

@app.route('/')
def index():
  return 'You\'re on index page'

if __name__ == '__main__':
  app.run()
