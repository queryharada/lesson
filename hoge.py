from flask import Flask, jsonify, abort, make_response, render_template, request
from flask_cors import CORS

api = Flask(__name__)
CORS(api)  # CORS有効化


@api.route('/get', methods=['GET'])  # Getだけ受け付ける
def get():  # 関数名は重複していなければなんでもよい
    result = ""
    # ローカルのファイルを全部読み込んで返すだけ
    with open("./datafile", mode='r') as f:
        result += f.read()
    return result


@api.route('/post', methods=['POST'])  # Postだけ受け付ける
def post():
    result = request.form["param"]  # Postで送ったときのパラメータの名前を指定する
    # パラメータをローカルのファイルに書き込むだけ
    with open("./datafile", mode='a') as f:
        f.write(result + "\n")
    return make_response(result)

@api.route('/')
def index():
    return render_template('index.html')



# 4000番ポートでWebサーバを起動する
if __name__ == '__main__':
    api.run(host='127.0.0.1', port=4000, debug=True)
