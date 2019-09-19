from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """<!DOCTYPE html><html><head><meta charset="utf-8"/><link rel="stylesheet" href="/static/style.css"/></head><body><h1>Hello World</h1></body></html>"""

@app.route('/title/<title>')
def title(title):
    return render_template('index.html', title=title)

@app.route('/user/<int:user_id>')
def user_id(user_id):
    return 'user_id:' + str(user_id).rjust(6)

@app.route('/search')
def search():
    q = request.args.get('q', '')
    return 'q: ' + q

@app.route('/login', methods=['GET'])
def render_from():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] and request.form['email']:
        return render_template('check.html', email=request.form['email'],
                                            username=request.form['username'])
    else:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(debug=True)
