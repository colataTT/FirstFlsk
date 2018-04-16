from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel'}
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''
@app.route("/hello")
def hello():
    user = { 'name' : 'world!' }
    return render_template("index.html",
                           title = 'hello',
                           user = user)