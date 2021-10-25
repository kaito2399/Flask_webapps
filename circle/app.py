#flaskの全てをインポートする
from flask import *

#Flaskクラスをインスタンス化して変数appに割り当てる

import calculation_circle
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

#変更&追加-----------------------
@app.route("/calc", methods=['GET','POST'])
def calc():
	if request.method == 'GET':
		return render_template('calc.html')
	elif request.method == 'POST':
		diameter = request.form['diameter']
		result = calculation_circle(diameter)
		if len(result) == 2:
			return render_template('calc.html', area=result[0],circumference=result[1])
		else:
			return render_template('calc.html',error=result)
#-------------------------------------
	

if __name__ == '__main__':
    app.run()