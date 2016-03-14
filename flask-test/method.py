
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return 'hello, getter!'
  else:
    return 'hello, poster!'

if __name__ == '__main__':
  app.run()
