#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import traceback
import json

# from flask import Flask

from flask import Flask,render_template,request,redirect,session
from urllib import urlencode,quote,unquote


app = Flask(__name__,template_folder="../templates")
app.secret_key = "sdsfdsgdfgdfgfh"   # 设置session时，必须要加盐，否则报错





#测试1  基本使用
@app.route('/')
def hello_world():
    return 'Hello World!'



#测试2  绑定路由的方法
#添加路由关系的本质：将url和视图函数封装成一个Rule对象，添加到Flask的url_map字段中
# curl "http://127.0.0.1:5000/index.html" -X POST -v
# curl "http://127.0.0.1:5000/index.html" -X GET -v

#绑定路由的第一种方式
@app.route('/index.html',methods=['GET','POST'],endpoint='index_function')  #这里的 endpoint 是 前面 '/index.html' 的别名
def index_function():
    return 'Index'


#绑定路由的第二种方式
def index2_function():
    return "Index2\n"
#app.add_url_rule(rule='/index2.html', endpoint="index", view_func=index2_function,methods=["GET", "POST"])

#变种
app.add_url_rule(rule='/index2.html', endpoint="index", view_func=index2_function, methods=["GET", "POST"])
app.view_functions['/index2.html'] = index2_function
#app.view_functions['index'] = index2_function





#测试3  Flask中的装饰器
#测试3  自己定义的装饰器
def wrapper(func):
    def inner(*args,**kwargs):
        if not session.get("user_info"):
            return redirect("/login")
        ret = func(*args,**kwargs)
        return ret
    return inner


@app.route("/login",methods=["GET","POST"])  # 指定该路由可接收的请求方式，默认为GET
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        print(request.values)   #这个里面什么都有，相当于body
        username = request.form.get("username")#post  获取参数
        password = request.form.get("password")
        print username,password
        if username=="haiyan" and password=="123":
            session["user_info"] = username
            # session.pop("user_info")  #删除session
            return redirect("/_index")
        else:
            # return render_template("login.html",**{"msg":"用户名或密码错误"})
            return render_template("login.html",msg="用户名或者密码错误")


@app.route("/_index",methods=["GET","POST"])
@wrapper    #自己定义装饰器时，必须放在路由的装饰器下面
def index():
    # if not session.get("user_info"):
    #     return redirect("/login")
    login_params()
    return render_template("index.html")



#测试4 获取url参数



def login_params():
    if request.method == 'GET':
        s1 = request.args
        s2 = request.args.to_dict()
        s3 = urlencode(s1)
        s4 = urlencode(s2)
        s5 = unquote(s3)
        s6 = unquote(s4)
        s7 = quote("胡冲")
        print('s1',s1)
        print('s2',s2)
        print('s3',s3)
        print('s4',s4)
        print('s5',s5)
        print('s6',s6)
        print('s7',s7)

        return render_template('login.html')

@app.route('/____index.html',methods=['GET','POST'],endpoint='____index')  #这里的 endpoint 是 前面 '/index.html' 的别名
def __index_function():
    login_params()
    return "SSS"


#测试5  flask 配置文件

#方式一：PS： 由于Config对象本质上是字典，所以还可以使用app.config.update(...)
app.config['DEBUG'] = False



if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
