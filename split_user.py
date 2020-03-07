from flask import Flask,session

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello from the simple web app'

@app.route('/login')
def do_logon() -> str:
    session['logged_in'] = True
    return 'You are now logged in'

@app.route('/page1')
def page1() -> str:
    return "page 1"

@app.route('/page2')
def page2() -> str:
    return "page 2"

@app.route('/page3')
def page3() -> str:
    return "page 3"

@app.route('/logout')
def logout() -> str:
    session.pop('logged_in', None)
    return 'Now you logged out'

@app.route('/status')
def status() -> str:
    if 'logged_in' in session:
        return 'You are currently logged in'
    return 'You are NOT logged in'



app.secret_key = 'Try something do'

if __name__ == '__main__':
    app.run(debug = True)