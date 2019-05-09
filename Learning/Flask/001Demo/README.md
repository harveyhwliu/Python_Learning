
 ### 一、Flask介绍（轻量级的框架)
 
 Flask是一个基于Python开发并且依赖jinja2模板和Werkzeug WSGI服务的一个微型框架，对于Werkzeug本质是Socket服务端，其用于接收http请求并对请求进行预处理，然后触发Flask框架，开发人员基于Flask框架提供的功能对请求进行相应的处理，并返回给用户，如果要返回给用户复杂的内容时，需要借助jinja2模板来实现对模板的处理，即：将模板和数据进行渲染，将渲染后的字符串返回给用户浏览器。

  
 ### 二、安装： 
 pip3 install Flask


 ### 三、基础使用
 
  1.  Flask实例
  ```
     from flask import Flask 
     app = Flask(__name__)  # 这是实例化一个Flask对象，最基本的写法
     
     
     #Flask实例中还有其他参数，以下是可填的参数，及其默认值
     def __init__(self, import_name, static_path=None, static_url_path=None,
                 static_folder='static', template_folder='templates',
                 instance_path=None, instance_relative_config=False,
                 root_path=None):
                 
  ``` 
  2.  绑定路由关系的两种方式 （添加路由关系的本质：将url和视图函数封装成一个Rule对象，添加到Flask的url_map字段中）
  ```
    #方式一  测试OK  | curl "http://127.0.0.1:5000/index.html" -X POST -v
    @app.route('/index.html',methods=['GET','POST'],endpoint='index_function')   #endpoint 这里就是 '/index.html' 的别名
    def index_function():
        return 'Index'
            
    #方式二  测试Ok ,这里的self 就是指 Flask 实例 等价于app (app = Flask(__name__))
    def index_func():
        return "Index"
    self.add_url_rule(rule='/index.html', endpoint="index", view_func=index_func, methods=["GET","POST"]) 
    or
    
    app.add_url_rule(rule='/index.html', endpoint="index", view_func=index_func, methods=["GET","POST"])
    app.view_functions['index'] = index_func

  ```
  3. 装饰器 
  ```
    from flask import Flask,render_template,request,redirect,session


    app = Flask(__name__,template_folder="../templates")  #需要指明templates的位置
    app.secret_key = "sdsfdsgdfgdfgfh"   # 设置session时，必须要加盐，否则报错
    
    
    def wrapper(func):
        def inner(*args,**kwargs):
            if not session.get("user_info"):         #判断session是否正常，不正常重定向到登陆页面
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
            username = request.form.get("username")
            password = request.form.get("password")
            print username,password
            if username=="haiyan" and password=="123":
                session["user_info"] = username
                # session.pop("user_info")  #删除session
                return redirect("/_index")       #验证通过 重定向 /_index
            else:
                # return render_template("login.html",**{"msg":"用户名或密码错误"})
                return render_template("login.html",msg="用户名或者密码错误")
    
    
    @app.route("/_index",methods=["GET","POST"])
    @wrapper    #自己定义装饰器时，必须放在路由的装饰器下面
    def index():
        # if not session.get("user_info"):
        #     return redirect("/login")
        return render_template("index.html")           #这里index.html login.html 都是需要放到templates中的
        
  ```  
  4. 获取GET参数
  ```
    #测试用例：curl "http://127.0.0.1:5000/____index.html?sssssssssssssdf=asdf&sdfasdf=safdssssssssssssssssssssssssss" -X GET -v
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
  ```
  
  
