from flask import *

# Flaskオブジェクトの生成
app = Flask(__name__)

# ルート( / )へアクセスがあった時 --- (*1)
@app.route("/")
def index():
    return render_template('index.html')

import calculation
from calculation import seki
# フォームの値を受け取って結果を表示 --- (*3)
@app.route("/calc", methods=["post"])
def calc():
    a = int(request.form.get("a"))
    b = int(request.form.get("b"))
    return seki(a,b)

# サーバーを起動
if __name__ == "__main__":
    app.run(debug=True, port=8888)