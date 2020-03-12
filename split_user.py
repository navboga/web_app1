from flask import Flask,session
from checker import check_logged_in

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello from the simple web app'

@app.route('/login')
def do_logon() -> str:
    session['logged_in'] = True
    return 'You are now logged in'

@app.route('/page1')
@check_logged_in
def page1() -> str:
    return "page 1"

@app.route('/page2')
@check_logged_in
def page2() -> str:
    return "page 2"

@app.route('/page3')
@check_logged_in
def page3() -> str:
    return "page 3"

@app.route('/logout')
def logout() -> str:
    session.pop('logged_in', None)
    return 'Now you logged out'


app.secret_key = 'Try something do'

if __name__ == '__main__':
    app.run(debug = True)