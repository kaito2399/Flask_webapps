from flask import *
from pulp_calc import calc_min_bin, calc_max_bin
import os
# Flaskオブジェクトの生成
app = Flask(__name__)

key = os.urandom(21)
app.secret_key =key

# ルート( / )へアクセスがあった時
@app.route("/")
def index():
    return render_template('index.html')

#設定を入力
@app.route("/setting")
def setting():
    return render_template('setting.html')


# 変数の数を入力
@app.route("/input", methods=['POST'])
def input():
    sense = request.form["sense"]
    v = request.form["var"]
    cat = request.form["cat"]
    ineq = request.form['ineq']
    eq = request.form["eq"]
    if v.isdigit() and ineq.isdigit() and eq.isdigit():
        var_size=int(v)
        ineq_size=int(ineq)
        eq_size=int(eq)
        session['sense'] = sense
        session["var_size"] = var_size
        session["cat"] = cat
        session["ineq_size"] = ineq_size
        session["eq_size"] = eq_size
        return render_template('input.html', var=var_size, ineq=ineq_size, eq=eq_size)
    else:
        again=True
        return render_template('setting.html', again=again)

@app.route("/calc", methods=['POST'])
def calc():
    var_size = session.get('var_size')
    ineq_size = session.get('ineq_size')
    eq_size = session.get('eq_size')
    C = [(request.form["c{}".format(i)]) for i in range(var_size)]
    A=[]
    for j in range(ineq_size):
        a=[(request.form["a{}{}".format(j,i)]) for i in range(var_size)]
        if all([i.isdigit() for i in a]):
            A.append(list(map(int,a)))
        else:
            again=True
            return render_template('input.html', again=again, var=var_size, ineq=ineq_size, eq=eq_size)
            break
    E=[]
    for j in range(eq_size):
        e=[(request.form["e{}{}".format(j,i)]) for i in range(var_size)]
        if all([i.isdigit() for i in e]):
            E.append(list(map(int,e)))
        else:
            again=True
            return render_template('input.html', again=again, var=var_size, ineq=ineq_size, eq=eq_size)
            break
    B = [(request.form["b{}".format(j)]) for j in range(ineq_size)]
    F = [(request.form["f{}".format(j)]) for j in range(eq_size)]
    if all([i.isdigit() for i in C]) and all([i.isdigit() for i in B]) and all([i.isdigit() for i in F]):
        sense = session.get('sense')
        cat = session.get('cat')
        if sense=='min':
            if cat=='bin':
                status,objective,kai= calc_min_bin(list(map(int,C)), A, list(map(int,B)), E, list(map(int,F)))
            elif cat=='con':
                status,objective,kai= calc_min_con(list(map(int,C)), A, list(map(int,B)), E, list(map(int,F)))
            else:
                status,objective,kai= calc_min_int(list(map(int,C)), A, list(map(int,B)), E, list(map(int,F)))
        
        else:
            if cat=='bin':
                status,objective,kai= calc_max_bin(list(map(int,C)), A, list(map(int,B)), E, list(map(int,F)))
            elif cat=='con':
                status,objective,kai= calc_max_con(list(map(int,C)), A, list(map(int,B)), E, list(map(int,F)))
            else:
                status,objective,kai= calc_max_int(list(map(int,C)), A, list(map(int,B)), E, list(map(int,F)))
        
        
        
        return render_template('result.html', status=status, objective=objective,kai=kai)







# サーバーを起動
if __name__ == "__main__":
    app.run(debug=True)