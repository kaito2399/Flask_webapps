from flask import *
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


#インスタンスの作成
app = Flask(__name__)

#暗号かぎの作成
key = os.urandom(21)
app.secret_key =key

#idとパスワードの設定
id_pwd={'Conan': 'Heiji'}

#データベース設定
URI = 'postgres:lsoyp23@localhost/flasktest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']=URI
db=SQLAlchemy(app)

#テーブル内容の設定
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), index=True, unique=True)
    file_path = db.Column(db.String(64), index=True, unique=True)
    dt = db.Column(db.DateTime, nullable=False, default=datetime.now)

#テーブルの初期化
@app.cli.command('initdb')
def initdb():
    db.create_all()

#メイン
@app.route('/')
def index():
    if not session.get('login'):
        return redirect(url_for('login'))
    else:
        return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logincheck', methods=['POST'])
def logincheck():
    user_id = request.form['user_id']
    password = request.form['password']

    if user_id in id_pwd:
        if password == id_pwd[user_id]:
            session['login'] = True
        else:
            session['login'] = False
    else:
        sesion['login'] = False

    if session['login']:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('login', None)#Noneはデフォルト値でキーが存在しなかったときNoneを返す
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)