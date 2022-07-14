from flask import Flask
from flask.globals import request
from flask.templating import render_template
from day12.daoemp import DaoEmp
from flask.json import jsonify

app = Flask(__name__,static_url_path='')


@app.route('/')
@app.route('/emp')
def emp_list():
    return render_template('emp.html')

@app.route('/ajaxlist', methods=['POST'])
def ajaxlist():
    de = DaoEmp()
    list = de.selects()
    return jsonify(list)
    # return jsonify({'list': list}) #이렇게도 됨
    
@app.route('/ajaxone', methods=['POST'])
def ajaxone():
    e_id = request.form['e_id']
    de = DaoEmp()
    emp = de.select(e_id)
    return jsonify(emp) # list는 json형태라서 emp만 넘겨도 됨
    
@app.route('/ajaxadd', methods=['POST'])
def ajaxadd():
    e_name = request.form['e_name']
    sex = request.form['sex']
    addr = request.form['addr']
    de = DaoEmp()
    cnt = de.insert(e_name, sex, addr)
    return jsonify({"cnt":cnt}) # json형태로 만들어서 넘겨줌
    
@app.route('/ajaxmod', methods=['POST'])
def ajaxmod():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    sex = request.form['sex']
    addr = request.form['addr']
    de = DaoEmp()
    cnt = de.update(e_id, e_name, sex, addr)
    return jsonify({"cnt":cnt})

@app.route('/ajaxdel', methods=['POST'])
def ajaxdel():
    e_id = request.form['e_id']
    de = DaoEmp()
    cnt = de.delete(e_id)
    return jsonify({"cnt":cnt})

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    