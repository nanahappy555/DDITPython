from flask import Flask
from flask.globals import request
from flask.templating import render_template
from day10.daoemp import DaoEmp

app = Flask(__name__)


@app.route('/')
@app.route('/emp_list')
def emp_list():
    de = DaoEmp()
    list = de.selects()
    
    return render_template('emp_list.html',list=list)

@app.route('/emp_detail')
def emp_detail():
    e_id = request.args.get('e_id')
    de = DaoEmp()
    emp = de.select(e_id)
    
    return render_template('emp_detail.html', emp=emp)

@app.route('/emp_mod')
def emp_mod():
    e_id = request.args.get('e_id')
    de = DaoEmp()
    emp = de.select(e_id)
    
    return render_template('emp_mod.html', emp=emp)

@app.route('/emp_mod_act',methods=['POST','GET'])
def emp_mod_act():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    sex = request.form['sex']
    addr = request.form['addr']
    de = DaoEmp()
    cnt = de.update(e_id,e_name,sex,addr)
    
    return render_template('emp_mod_act.html', cnt=cnt)

@app.route('/emp_add')
def emp_add():
    e_id = request.args.get('e_id')
    de = DaoEmp()
    emp = de.select(e_id)
    
    return render_template('emp_add.html', emp=emp)

@app.route('/emp_add_act')
def emp_add_act():
    e_id = request.args.get('e_id')
    de = DaoEmp()
    cnt = de.insert(e_id)
    
    return render_template('emp_add_act.html', cnt=cnt)

@app.route('/emp_del')
def emp_del():
    e_id = request.args.get('e_id')
    de = DaoEmp()
    emp = de.select(e_id)
    
    return render_template('emp_add.html', emp=emp)

@app.route('/emp_del_act')
def emp_el_act():
    e_id = request.args.get('e_id')
    de = DaoEmp()
    cnt = de.delete(e_id)
    
    return render_template('emp_del_act.html', cnt=cnt)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    