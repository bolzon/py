
from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)

@app.route('/')
def index():
  if 'username' in session:
    return 'Logged in as %s: <a href="/logout">logout</a>' % escape(session['username'])
  return 'You\'re not logged in: <a href="/login">login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    session['username'] = request.form['username']
    return redirect(url_for('index'))
  return '''
    <form action="" method="post">
      <input type="text" name="username"/>
      <input type="password" name="password"/>
      <input type="submit"/>
    </form>
  '''

@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('index'))

# the app secret key
app.secret_key = '7e690131a147be3fa75ef0e4832baa10858f29d2e73cd1fafbf0bc17b2337889'

if __name__ == '__main__':
  app.run()
