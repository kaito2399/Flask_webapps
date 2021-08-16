from flask import *
import os
from haibun_calc import haibun
# Flaskオブジェクトの生成
app = Flask(__name__)

key = os.urandom(21)
app.secret_key =key

# ルート( / )へアクセスがあった時
@app.route("/")
def index():
    return render_template('index.html')

# オッズを入力
@app.route("/input", methods=['POST'])
def input():
    n = request.form["n"]
    if n.isdigit():
        n_size=int(n)
        session["n_size"] = n_size
        return render_template('input.html', n=n_size)
    else:
        again=True
        return render_template('index.html', again=again)

@app.route("/calc", methods=['POST'])
def calc():
    n_size = session.get('n_size')
    O = [(request.form["odds{}".format(i)]) for i in range(n_size)]
    O =sorted(O)
    A = (request.form["shikin"])
    if all([i.isdigit() for i in O]) and A.isdigit():
        status,min_haibun,hm = haibun(O,int(A))
        return render_template('result.html', status=status, min_haibun=min_haibun,hm=hm)
    else:
        again=True
        return render_template('input.html', again=again, n=n_size)


# サーバーを起動
if __name__ == "__main__":
    app.run(debug=True)