from flask import Flask
from flask import request
from flask.templating import render_template
from day09.daoemp import DaoEmp
app = Flask(__name__)


@app.route('/')
def hello_word():
    return 'Hello Flask'

#get방식
@app.route('/para')
def para():
    p = request.args.to_dict() # {"a":"555"}
    # p = request.args.get('a') # 555 # 매개변수에 'p'라고 써도 실행은 되지만 None이라고 나옴
    return f'parameter : {p}'

@app.route('/<pagename>')
def hello(pagename):
    return 'hello' + pagename

# post방식
@app.route('/post',methods=['POST'])
def post():
    name = request.form['a']
    return 'POST' + name

@app.route('/dyna')
def dyna():
    a = '홍길동'
    b = ['홍길동','전우치','이순신']
    c = [
        {'e_id':'1','e_name':'1','sex':'1','addr':'1'},
        {'e_id':'2','e_name':'2','sex':'2','addr':'2'},
        {'e_id':'3','e_name':'3','sex':'3','addr':'3'}
        ]
    return render_template('dyna.html',a=a, b=b, c=c)

@app.route('/emp_list')
def emp_list():
    de = DaoEmp()
    list = de.selects()
    return render_template('emp_list.html',list=list)

if __name__ == '__main__':
    app.run()
    
    