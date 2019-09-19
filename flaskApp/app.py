from flask import Flask, request
from flask import render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', obj={"title": "hoge"})


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


@app.route('/upload', methods=['GET'])
def render_upload_form():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.form['name'] and request.files['image']:
        f = request.files['image']
        filepath = 'static/' + secure_filename(f.filename)
        f.save(filepath)
        return render_template('result.html', name=request.form['name'])


if __name__ == "__main__":
    app.run(debug=True)
