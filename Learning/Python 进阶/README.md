## 0、重要的Python 库
   0. pip安装包，-i指定源，-t指定安装路径，推荐大家使用豆瓣的源

   ```python
      1. pip install matplotlib==2.2.4  -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
      2. pip install numpy -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
      3. pip install pandas  -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
      4. pip install seaborn scipy==1.2.0  -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
      5. pip install -t /usr/local/lib/python2.7/site-packages/ future  安装了多版本python时，pip安装的包不一定是用户想要的位置，此时可以用 -t 选项来指定位置
```

   1. Numpy (Numerical python) python 科学计算的基础包

   ```python
      1. python -m pip list 查看 
      2. python -m pip install --upgrade pip 更新 
      3. python -m pip install numpy 安装  （使用豆瓣的源）
```

   2. Pandas 快速处理结构化数据的大量数据结构和函数  + DataFrame
      1. 安装前，需要安装Cython或者升级Cython先   pip install Cython
      
   3. Matplotlib 最流行的绘图数据图表的python库
   4. Scipy  包括统计,优化,整合,线性代数模块,傅里叶变换,信号和图像处理,常微分方程求解器等等

## 1、 python 2 和 python 3 的区别
   1. https://wiki.python.org/moin/Python2orPython3
   2. https://www.cnblogs.com/weikunzz/p/6857971.html
   3. https://blog.csdn.net/weixin_41819299/article/details/81259721
   4. filter map 函数Python2返回的是可迭代对象Iteratable，而Python3 返回的迭代器Iterator,需要通过list()来转一下,且python3 需要通过from functools import reduce 导入reduce,python2 则不需要的
   5. type返回结果的类型有区别了，例如 type("ss") ，python2 返回结果是<type 'str'>,python3 返回结果是<class 'str'>
   6. python3取消了python2中dict的if _dict_obj.has_key(key)的方法，python3中使用if key in _dict_obj:
   7. python3 dict没有iteritems(),只能使用items()
   8. python2 中tuple用()来定义，python3中使用{}来定义
   9. 对于生成器generator c来说,python 2 可以使用c.next() 但是python3 只能使用next(c)

## 2、*args 和 **kwargs的区别
### 1） 基本用法
   1. 用来给函数传参，标准参数与*args、**kwargs在使用时的顺序为：`some_func(fargs1，...fargsn, *args, **kwargs)`
   2. *args 和 **kwargs 不是关键字，可以替换成成其他合法变量名
   3. *args 是一个list，可以采用some_func(*args)传递参数，但是这个list的长度必须大于等于some_func的标准形参个数，多余的参数放到函数args中
   4. *kwargs是一个dict,可以采用some_func(**kwargs)传递参数，但这个dict的key必须全部包括some_func形参的名，否则会报错，多余的部分放到函数kwargs这个dict中
### 2）使用场合
   1. 不知道用户传递的参数有多少
   2. monkey patching,只是在程序运行时(runtime)修改某些代码。 打个比方，你有一个类，里面有个叫get_info的函数会调用一个API并返回相应的数据。如果我们想测试它，可以把API调用替换成一些测试数据`obj.func = _nws_func`
   3. 最常见的用例是在写函数装饰器的时候
   
## 3、 调试代码 pdb
### 1） 基本用法
   1. 从命令上执行调试命令：python -m pdb my_script.py，会触发debugger在脚本第一行指令处停止执行。这在脚本很短时会很有帮助。
   2. 可以在脚本内部设置断点，通过首先导入pdb模块，然后在关键点处：使用pdb.set_trace() 设置断点
   3. 常用pdb命令：
     -. c: continue 或 c	继续执行程序    
     -. w: 显示当前正在执行的代码行的上下文信息  
     -. a: 打印当前函数的参数列表  
     -. s: 执行当前代码行，并停在第一个能停的地方（进入函数)  
     -. n: 继续执行到当前函数的下一行，或者当前行直接返回（单步跳过）  
     -. p:打印内容  
     -. break 或 b 设置断点	设置断点    
     -. list 或 l	查看当前行的代码段    
     -. return 或 r	执行代码直到从当前函数返回    
     -. exit 或 q	中止并退出      
     -. help	帮助   

### 2）使用场合
   1. 一种交互的源代码调试功能，主要特性包括设置断点、单步调试、进入函数调试、查看当前代码、查看栈片段、动态改变变量的值等 

## 4、 Generators 生成器
### 1） 基本用法
   1. 可迭代对象(Iterable) 比如list,str 就是能提供迭代器的任意对象，Python中任意的对象，只要它定义了可以返回一个迭代器的__iter__方法，或者定义了可以支持下标索引的__getitem__方法，就是可迭代对象。  
   2. 迭代器(Iterator),任意对象，只要定义了next(Python2) 或者__next__方法，它就是一个迭代器。
   3. 迭代(Iteration)，简单说，就是从某个地方（比如一个列表）取出一个元素的过程。当我们使用一个循环来遍历某个东西时，这个过程本身就叫迭代。
   4. 生成器(Generators) 也是一种迭代器，但是你只能对其迭代一次。这是因为它们并没有把所有的值存在内存中，而是在运行时生成值。你通过遍历来使用它们，要么用一个“for”循环，要么将它们传递给任意可以进行迭代的函数和结构。大多数时候生成器是以函数来实现的。然而，它们并不返回一个值，而是yield(暂且译作“生出”)一个值
   5. 通过yield返回一个generator 对象，运行时才生成结果值
   6. Python内置函数：next()。它允许我们获取一个Iterator的下一个元素，实际上是yield返回所有元素后，再次调用 next()触发了一个StopIteration的异常，for循环会自动捕捉到这个异常并停止调用next()。
   7. Python内置函数，iter。它将根据一个可迭代对象返回一个迭代器对象,比如print next(iter([1,2,3]))
   
### 2）使用场合
   1. 节省内存，生成器最佳应用场景是：你不想同一时间将所有计算出来的大量结果集分配到内存当中，特别是结果集里还包含循环。

## 5、 MAP Filter reduce
### 1） 基本用法
   1. Map会将一个函数映射到一个输入列表的所有元素上。这是它的规范：map(function_to_apply, list_of_inputs),举例：`list(map(lambda x: x**2, [1,2,3,4,5]))`
   2. filter过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表，符合要求即函数映射到该元素时返回值为True,`filter(lambda x:x>0,[0,1,2,3])`
   3. 当需要对一个列表进行一些计算并返回结果时，Reduce 是个非常有用的函数,举例：`reduce(lambda x,y:x+y,[1,2,3,4,5,6,7,8,9])#求列表的各项元素之和`


### 2）使用场合
   1. 简化代码，提高效率，例如对list的处理上取代for循环

## 6、 set的使用
### 1） 基本用法
   1. set不能包含重复的值,例如对查找重复的元素：`print(list(set([x for x in [1,2,3,2] if [1,2,3,2].count(x)>1])))`
   2. set用来求两个序列的交集：`print(set(a).intersection(set(b)))`
   3. set用来求两个序列中不交叉的数据集：`print(set(a).difference(set(b)))  #在a序列但不在b序列中的元素集`


### 2）使用场合
   1. 通过set不能包含重复元素的特性，实现业务侧查重、查交集、查差集的需求

## 7、python中的三元运算符
### 1） 基本用法
   1. 三元运算符是基于条件表达式真假的条件判断，python2.4以上才支持，举例：`x=0 if x in pid_l else pid_l[x]`
   2. 切记使用`print((1/0,11)[condition]) `这种元组条件表达式，因为元素是先建立数据，再利用下标索引来查找数据，因此在元组中所有条件都执行

### 2）使用场合
   1. 省略多余的if表达式，可以使代码简单可维护
   2. 如果逻辑中的条件异常，或者是重计算型（计算较久）的情况下，最好尽量避免使用元组条件表达式

## 8、decorators 装饰器
### 1） 基本用法
   1. decorators 是修改其他函数的功能的函数。他们有助于让在对已有函数进行功能扩充，也更Pythonic（Python范儿）
   2. 可以在函数中定义另外的函数。也就是说：我们可以创建嵌套的函数,并可以在外层函数中返回其内内嵌函数；函数也可以作为实参传递给另外函数的形参例如`printNum(getNum) #这里getNum是一个函数`
   3. 直接采用函数内嵌的方式返回，发现采用注解前后，本质上是函数的名字和注释文档docstring已经发生了重写。使用`from functools import wraps 中@wraps(func)  `@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。

### 2）使用场合
   1. 不改变原来函数的基础上，加上一些新的功能，比如日志，耗时分析等等
   2. 实际应用举例： 计算函数耗时时间的装饰器

   ```python
    def decorator_calc_cost_time(func):  #装饰器的名字
        start_time = time.time()
        @wraps(func)                     #采用@wraps，接收原来函数的名称，注释文档，以及参数列表中
        def decorated(*args,**kwargs):   #通过函数内嵌来实现
            res = func(*args,**kwargs)   #得到原来函数的返回结果并返回
            print("%.3fs"%(time.time()-start_time))
            return res
        return decorated                 #返回内嵌函数名

    #这就是一个装饰器
    @decorator_calc_cost_time
    def function3(a,b):
        print("I am function3()")
        time.sleep(a*b)
``` 

   3. 业务应用场景： web应用端点（endpoint）的访问鉴权（Flask和Django web框架） 
   4. @wraps 也是装饰器，但他接收一个参数，就像任何普通函数那样为什么我们不这样做呢？  因为当使用@my_decorator语法时，是在应用一个以单个函数作为参数的一个包裹函数。创建一个包裹函数，举例如下：

   ```python
    #创建一个包裹函数  包裹函数其实是对函数进行封装。将所有可能出现的情况写在一起，以便于程序的调用，提高程序的可读性
    def logit(logfile='out.log'):
        def logging_decorator(func):
            @wraps(func)
            def warppend_function(*args,**kwargs):
                log_string = "{0} was called\n".format(func.__name__)
                with open(logfile,'a') as fd:
                    fd.write(log_string)
                return func(*args,**kwargs)
            return warppend_function
        return logging_decorator

    @logit()
    def my_test1():
        pass
    @logit(logfile="access.log")
    def my_test2():
        pass
```

   5. 装饰器类,进一步对装饰器的功能进行扩展,@email_logit将会和@decorator_logit_c产生同样的效果，但会多一个notify指定的新功能

   ```python
    class decorator_logit_c(object):#基类
        def __init__(self,logfile="out.log"):
            self.logfile = logfile

        def __call__(self,func):
            @wraps(func)
            def wrapped_function(*args,**kwargs):
                log_string = "{0} was called\n".format(func.__name__)
                with open(self.logfile,'a') as fd:
                    fd.write(log_string)
                return func(*args,**kwargs)
            return wrapped_function

        def notify(self):
            pass#基类只进行日志打印功能

    class email_logit(decorator_logit_c):#子类，在函数调用时发送email给管理员
        def __init__(self, email='', logfile="out2.log"):
            self.email = email
            self.logfile = logfile
            super(decorator_logit_c, self).__init__()

        def notify(self):
            # 发送一封email到self.email
            # 这里就不做实现了
            pass

    @decorator_logit_c(logfile="a.log")
    def my_test3():
        pass

    @email_logit(email="2580205897@qq.com",logfile="access2.log")
    def my_test4():
        pass
```

## 9、global  return的使用
### 1） 基本用法
   1. global 变量名， 在局部作用域中创建或者声明了一个全局变量，不能声明的时候赋值（global res = a+b是错误的）应该是(global res ;res = a+B)
   2. 如果函数返回多个变量，应该如何做呢？ 一种是通过返回一个包含多个值得tuple,list或者dict来解决。另一种则是直接return var1,var2,..,varn

### 2）使用场合
   1. 应该避免使用global,因为global 将变量的作用域变成了全局作用域，产生问题的概率将会增大


## 10、mutable 和 immutable
### 1） 基本用法
   1. Python中可变(mutable)与不可变(immutable)的数据类型,string,float,integer,tuple是不可变类型，可变类型：list,dict （通过id()函数来看对象唯一ID）
   2. mutable 类型：变量名存储的是一个地址，该地址指向一个具体的对象，并且不管对变量的值即对象做怎么样的操作，都不会改变变量名存储的地址
   3. immutable 类型：不变数据类型的对象一旦发生改变，就会在内存中开辟一个新的空间用于存储新的对象，原来的变量名就会指向一个新的地址。
   4. 由于python规定参数传递都是传递引用，也就是传递给函数的是原变量实际所指向的内存空间，修改的时候就会根据该引用的指向去修改该内存中的内容，但由于有可变类型和不可变类型，这样的话，当传过来的是可变类型(list,dict)时，我们在函数内部修改就会影响函数外部的变量。而传入的是不可变类型时在函数内部修改改变量并不会影响函数外部的变量，因为修改的时候会先复制一份再修改。

### 2）使用场合
   1. python只允许使用引用传递，但由于mutable和immutable的影响，函数传参时，只有list ,dict才会修改原来的内容，其他的不会

## 11、__slot__的使用
### 1） 基本用法
   1. Python中，每个类都有实例属性。默认情况下Python用一个字典来保存一个对象的实例属性，一方面，它允许我们在运行时去设置任意的新属性，另一方面，对于那些已知属性的小类来说，会浪费很多内存。
   2. 可以使用__slots__(插槽)告诉python 不使用字典而且只给一个固定集合的属性分配空间
   3. 可以时候用dir(对象),或者inspect模块（`import inspect`） inspect.getmember(对象)  查看对象属性，发现少了 __dict__ 属性

### 2）使用场合: 针对那些对内存比较在意的程序，但也存在如下的缺点：
   1. 每个继承的子类都要重新定义一遍__slots__
   2. 实例只能包含哪些在__slots__定义的属性，这对写程序的灵活性有影响，比如你由于某个原因新网给instance设置一个新的属性，比如instance.a = 1, 但是由于a不在__slots__里面就直接报错了，你得不断地去修改__slots__或者用其他方法迂回的解决
   3. 实例不能有弱引用（weakref）目标，否则要记得把__weakref__放进__slots__
   4. weakref号称可以解决循环引用gc，Python使用了垃圾回收器来自动销毁那些不再使用的对象。每个对象都有一个引用计数，当这个引用计数为0时Python能够安全地销毁这个对象。使用weakref模块，你可以创建到对象的弱引用，Python在对象的引用计数为0或只存在对象的弱引用时将回收这个对象

## 11、virtual-env 虚拟环境
### 1） 基本用法
   1. Virtualenv 是一个工具，它能够帮我们创建一个独立(隔离)的Python环境。从而实现python版本库的隔离等需求
   2.

   ```python
    pip install virtualenv  #安装virtual-env
    virtualenv my_proj_name #创建一个文件夹 my_proj_name 来创建一个virtualenv 环境
    source my_proj_name/bin/activate #激活这个隔离环境 virtualenv
    deactivate              #退出virtualenv,运行之后将恢复使用系统全局的Python模块


    ps : 默认情况下，virtualenv不会使用系统全局模块。
    virtualenv --system-site-packages my_proj_name  #使用--system-site-packages参数  让virtualenv使用系统全局模块


```

### 2）使用场合:
   1. 使用smartcd来帮助你管理你的环境，当你切换目录时，它可以帮助你激活（activate）和退出（deactivate）你的virtualenv github(https://github.com/cxreg/smartcd)
   2.

## 12、collections 容器的使用
### 1） 基本用法
   1. Python的一个模块，它包含许多容器数据类型，名字叫作collections，包括：
   - defaultdict
   - counter   #from collections import Counter   Counter是一个计数器，它可以帮助我们针对某项数据进行计数
   - deque     #from collections import deque     deque提供了一个双端队列，你可以从头/尾两端添加或删除元素，deque(maxlen=30)默认长度为30，超过30个元素将会从左（前）到右（尾）回滚。
   - namedtuple#from collections import namedtuple 以像字典(dict)一样访问namedtuple，但namedtuple是不可变的,却可以让你的元组变得自文档，namedtuple的每个实例没有对象字典，所以它们很轻量，与普通的元组比，并不需要更多的内存。这使得它们比字典更快
   - enum.Enum #from enum import Enum             class Species(Enum): cat =1 ;Species.cat

### 2）使用场合:
   1. 实际应用中按需选择，提升效率

## 13、enumerate 的使用
### 1） 基本用法
   1. 枚举(enumerate)是Python内置函数,允许我们遍历序列并自动计数，enumerate 第一参数是iterable，第二个元素是 开始计数的基准，默认为0

### 2）使用场合:
   1. for c, value in enumerate([1,2,3], 1):  #从1开始计算索引，不是从0开始计算
   2. list(enumerate("abcsdkskdfksfsf", 1))   #创建一个包括索引和对应索引位置元素值得元组序列


## 14、introspection 自省
### 1） 基本用法
   1. introspection 自省，内省，在计算机编程领域里，是指在运行时来判断一个对象的类型的能力，python内一切皆对象
   2. python 自省的最重要函数：
   - dir  : dir([1,2,3]),如果运行dir()而不传入参数，那么它会返回当前作用域的所有名字
   - type : type 函数返回一个对象的类型  type(dict)
   - id :   id()函数返回任意不同种类对象的唯一ID
   - inspect:获取活跃对象的信息,比如对象的成员等  `import inspect;print(inspect.getmembers(str))`

### 2）使用场合:
   1. 了解当前可用的函数，或者了解对象自身等场景

## 15、comprehensions 推导式
### 1） 基本用法
   1.  推导式是可以从一个数据序列构建另一个新的数据序列的结构体。 共有三种推导
   - 列表(list)推导式 ：list comprehensions 格式：`variable = [out_exp for out_exp in input_list if out_exp == 2]`
   - 字典(dict)推导式 : dict comprehensions 格式：统计字典中key的频数- `mcase={'a':1,'A':2,'c':3}；{k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys()}`
   - 集合(set)推导式  : set comprehensions  格式：`(x**2 for x in [1, 1, 2])`  python3要改为`{x**2 for x in [1, 1, 2]}`,否则返回的就是generator

### 2）使用场合:
   1. list comprehensions 在当你需要使用for循环来生成一个新列表使用，例如：`squared = [x**2 for x in range(10)]`
   2. dict comprehensions 快速替换value:key  `{v:k for k,v in {"a":1,"b":2}.items()}`

## 16、异常
### 1） 基本用法
   1. 基本的使用方式是：

   ```python
        try:
            file = open('test.txt', 'rb')
        except (IOError, EOFError) as e:
            print('An IOError occurred. {}'.format(e.args[-1]))
        except Exception as e:
            print('{}. {}'.format(e,traceback.format_exc())
            #raise  #如果需要抛出异常的化
        else:# 这里的代码只会在try语句里没有触发异常时运行,但是这里的异常将 *不会* 被捕获
            print('This would only run if no exception occurs. And an error here would NOT be caught.')
        finally:#不管异常是否触发都将会被执行,做一些退出前的清理操作，比如关闭mysql连接等等
            print("This would be printed whether or not an exception occurred!")


```

### 2）使用场合:
   1. 在for循环中采用try catch来提高效率，避免if条件判断的性能损失
   2. 处理多个异常时，可以采用所有可能发生的异常放到一个元组里，或者是对每个单独的异常在单独的except语句块中处理
   3. 包裹到finally从句中的代码不管异常是否触发都将会被执行。这可以被用来在脚本执行之后做清理工作。
   4. 在没有触发异常的时候执行一些代码。这可以很轻松地通过一个else从句来达到，else从句只会在没有异常的情况下执行，而且它会在finally语句之前执行

## 17、lambda 表达式
### 1） 基本用法
   1. lambda表达式是一行函数，也叫做匿名函数。格式:lambda 参数:操作(参数) , 就是一个函数，但这个函数只是临时使用一下的简单函数。

### 2）使用场合:
   1. 简化代码逻辑
   2. 常和map,filter ,reduce这些关键字一起使用

## 18、一行式
### 1） 基本用法
   1. 打印语句： `from pprint import pprint;pprint([1,2,3,4])`
   2. 快速漂亮的从文件打印出json数据  `cat json.json | python -m json.tool`
   3. 脚本性能分析： `python -m cProfile my_script.py ` #cProfile是一个比profile更快的实现，因为它是用c写的 TODO: 这里以后才补充
   4. CSV转换为json ：`python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"`
   5. 列表辗平：使用itertools包中的itertools.chain.from_iterable轻松快速的辗平一个列表  `list(itertools.chain.from_iterable([[1, 2], [3, 4], [5, 6]]))`
   6. 快速给类初始化，避免大量的赋值语句

   ```python
   class A(object):
        def __init__(self, a, b, c, d, e, f):# 相当于定义并初始化了self.a,self.b,..,self.f, 也可以通过self.__dict__["a"]这种方式来调用
            self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})

        def show():
            pprint("{0} {1} {2} {3} {4} {5}".format(self.a,self.b,self.c,self.d,self.e,self.f))
            pprint("{0} {1}".format(id(self.a),id(self.__dict__["a"])))

```

### 2）使用场合:
   1. 简化代码逻辑
   2. python 性能优化相关，比如cProfile profile hotshot等

## 19、for else的使用
### 1） 基本用法
   1. for 的else从句会在循环正常结束时执行。这意味着，循环没有遇到任何break

   ```python
    for item in [1,2,3,4,5,0]:
        if num == item:
            #TODO 做一些动作
            break
    else:
        #没有找到的时候做一些动作
        pprint("没有找到元素，遍历了整个序列后退出的")

```

### 2）使用场合:
   1. for else 常用在循环查找元素，区分是找到元素才退出还是遍历数据后没有知道才退出的



## 20、python 调用C代码
### 1） 基本用法
   1. 开发者有三种方法可以在自己的Python代码中来调用C编写的函数-，，
   - ctypes：Python中的ctypes模块可能是Python调用C方法中最简单的一种。
   1)  ctypes模块提供了和C语言兼容的数据类型和函数来加载dll文件，因此在调用时不需对源文件做任何的修改
   2)  ctypes接口允许我们在调用C函数时使用原生Python中默认的字符串型和整型。对于其他类似布尔型和浮点型这样的类型，必须要使用正确的ctype类型才可以
   3)  这种方法虽然简单，清晰，但是却很受限。例如，并不能在C中对对象进行操作


   ```python c

    #c函数代码 -- 生成so文件 linx : gcc -shared -Wl,-soname,adder -o adder.so -fPIC add.c
    #         --  For mac :      gcc -shared -Wl,-install_name,adder.so -o adder.so -fPIC add.c
    #include <stdio.h>

    int add_int(int num1, int num2){
        return num1 + num2;
    }

    float add_float(float num1, float num2){
        return num1 + num2;
    }

    from ctypes import *

    def test_demo1():
        adder = CDLL('./adder.so')                    #加载dll
        res_int = adder.add_int(4,5)
        print("Sum of 4 and 5 = " + str(res_int))

        adder.add_float.argtypes = (c_float, c_float) # add_float 有两个形参，都是 float 类型
        adder.add_float.restype = c_float             # add_float 返回值的类型是 float
        print("Sum of 5.5 and 4.1 = ", str(adder.add_float(5.5, 4.1)))

```

   - SWIG：SWIG是Simplified Wrapper and Interface Generator的缩写
   1） 在这个方法中，开发人员必须编写一个额外的接口文件来作为SWIG(终端工具)的入口。
   2） Python开发者一般不会采用这种方法，因为大多数情况它会带来不必要的复杂。
   3)  而当你有一个C/C++代码库需要被多种语言调用时，这将是个非常不错的选择

   ```c
   //----------------未经过测试 ----------------
    #include <time.h>
    double My_variable = 3.0;

    int fact(int n) {
        if (n <= 1) return 1;
        else return n*fact(n-1);

    }

    int my_mod(int x, int y) {
        return (x%y);

    }

    char *get_time()
    {
        time_t ltime;
        time(&ltime);
        return ctime(&ltime);
    }

    //swig 进行编译
    swig -python example.i
    gcc -c example.c example_wrap.c  -I/usr/local/include/python2.1
    ld -shared example.o example_wrap.o -o _example.so

    //python 输出：
    >>> import example
    >>> example.fact(5)
    120
    >>> example.my_mod(7,3)
    1
    >>> example.get_time()
    'Sun Feb 11 23:01:07 1996'

```

   - Python/C API：Python/C API可能是被最广泛使用的方法。它不仅简单，而且可以在C代码中操作你的Python对象
   1) 以特定方式来编写，所有的Python对象都被表示为一种叫做PyObject的结构体，并且Python.h头文件中提供了各种操作它的函数。例如，如果PyObject表示为PyListType(列表类型)时，那么我们便可以使用PyList_Size()函数来获取该结构的长度
   2)

   ```c  python

        #include <Python.h>
        //Python.h头文件中包含了所有需要的类型(Python对象类型的表示)和函数定义(对Python对象的操作)

        //编写将要在Python调用的函数, 函数传统的命名方式由{模块名}_{函数名}组成，所以我们将其命名为addList_add
        //参数类型为PyObject类型结构(同时也表示为元组类型，因为Python中万物皆为对象，所以我们先用PyObject来定义)
        static PyObject* addList_add(PyObject* self, PyObject* args){

            PyObject * listObj;

            //传入的参数则通过PyArg_ParseTuple()来解析。
            //第一个参数是被解析的参数变量。第二个参数是一个字符串，告诉我们如何去解析元组中每一个元素。
            //字符串的第n个字母正是代表着元组中第n个参数的类型。例如，"i"代表整形，"s"代表字符串类型, "O"则代表一个Python对象。
            //接下来的参数都是你想要通过PyArg_ParseTuple()函数解析并保存的元素。这样参数的数量和模块中函数期待得到的参数数量就可以保持一致，并保证了位置的完整性。
            /*
            例如，我们想传入一个字符串，一个整数和一个Python列表，可以这样去写
                int n;
                char *s;
                PyObject* list;
                PyArg_ParseTuple(args, "siO", &n, &s, &list);
            */
            if (! PyArg_ParseTuple( args, "O", &listObj ))
                return NULL;
            long length = PyList_Size(listObj);
            int i, sum =0;
            for (i = 0; i < length; i++) {
                //通过循环列表，使用PyList_GetItem(list, index)函数来获取每个元素。这将返回一个PyObject*对象。
                PyObject* temp = PyList_GetItem(listObj, i);
                //既然Python对象也能表示PyIntType，我们只要使用PyInt_AsLong(PyObj *)函数便转成C中的long对象
                long elem = PyInt_AsLong(temp);
                sum += elem;
            }
            //总和将被转化为一个Python对象并通过Py_BuildValue()返回给Python代码，这里的i表示我们要返回一个Python整形对象
            return Py_BuildValue("i", sum);

        }

        //This is the docstring that corresponds to our 'add' function.
        static char addList_docs[] =
        "add(  ): add all elements of the list\n";

        /* This table contains the relavent info mapping -
           <function-name in python module>, <actual-function>,
           <type-of-args the function expects>, <docstring associated with the function>
         */
        static PyMethodDef addList_funcs[] = {
            {"add", (PyCFunction)addList_add, METH_VARARGS, addList_docs},
            {NULL, NULL, 0, NULL}

        };

        /*
           填写想在模块内实现函数的相关信息表，每行一个函数，以空行作为结束 - 最后的模块初始化块签名为PyMODINIT_FUNC init{模块名}。
           <模块名>, <相关信息表>, <模块的文档>
         */
        PyMODINIT_FUNC initaddList(void){
            Py_InitModule3("addList", addList_funcs,"Add all ze lists");

        }

    // #build the modules   #保存到setup.py
    from distutils.core import setup, Extension
    setup(name='addList', version='1.0',ext_modules=[Extension('addList', ['pyobj.c'])])


   //并且运行  python setup.py install 将c文件编译安装到我们python 模块中

   //最后进行测试验证：
   #module that talks to the C code
    import addList

    l = [1,2,3,4,5]
    print "Sum of List - " + str(l) + " = " +  str(addList.add(l))

```

### 2）使用场合:
   1. 对性能要求高的部分，比如函数的执行部分可以用c实现，规避python全局锁，C要比Python快50倍以上
   2. C语言中有很多传统类库，而且有些正是你想要的，但你又不想用Python去重写它们
   3. 想对从内存到文件接口这样的底层资源进行访问

   4. ctypes 只能使用一个简单的场合，但其功能很受限。例如，并不能在C中对对象进行操作
   5. 如果c的代码可以被多种语言使用，可以采用swig的方式
   6.


## 21、open 的使用
### 1） 基本用法
   1.  with  open(file_name,'a') as fd:  可以规避几个问题：
   - 不需要显示的调用fd.close()关闭文件句柄
   - 避免采用文本模式写入时，没有调用flush()导致数据实际没有写入的问题
   2. 关于文件的编码，在Pyhon 2中，open不支持显示地指定编码。然而，io.open函数在Python 2.x中和3.x(其中它是open的别名)中都有提供，它能做正确的事。你可以传入encoding这个关键字参数来传入编码。

   ```python
    import io

    with open('th.jpeg', 'rb') as inf:
        jpgdata = inf.read()

    if jpgdata.startswith(b'\xff\xd8'):
        text = u'This is a JPEG file (%d bytes long)\n'
    else:
        text = u'This is a random file (%d bytes long)\n'

    with io.open('summary.txt', 'w', encoding='utf-8') as outf:
        outf.write(text % len(jpgdata))

```

   
### 2）使用场合:
   1. 使用with open() as fd 这种方式的处理文件操作


## 22、开发兼容Python2，3的程序
### 1） 基本用法
   1. 第一种也是最重要的方法，就是导入__future__模块。它可以帮你在Python2中导入Python3的功能。
   - from __future__ import print_function #导入print函数 <built-in function print>
   2. 脚本中对模块进行重命名,将模块导入代码包装在try/except语句中。导入失败后会引起引起一个ImportError异常。捕获到ImportError我们将通过导入正确的模块来代替它

   ```python
    try:
        import urllib.request as urllib_request     # for Python 3
    except ImportError:
        import urllib2 as urllib_request            # for Python 2
    print(urllib_request.localhost())
    
```

   3. 了解Python2中有12个内置功能在Python3中已经被移除了。要确保在Python2代码中不要出现这些功能来保证对Python3的兼容。
   - 这有一个强制让你放弃12内置功能的方法：`from future.builtins.disabled import *`
   - 需要安装future包，多python 版本时可以采用 -t 来指定安装路径，pip install -t /usr/local/lib/python3.7/site-packages/ future
   - apply()   在python2 中报错被提示已弃用，python3中报错为未定义

   4. 标准库向下兼容的外部支持。有一些包在非官方的支持下为Python2提供了Python3的功能
   - `enum` : pip install enum34    #Python 2.x 中是没有原生的枚举类型的,可以使用这个包class BugStatus(enum.Enum):定义枚举类，python3默认已经支持，直接导入import enum即可
   - `singledispatch` : pip install singledispatch  #提供单分派泛函数，即函数的重载功能
   - `pathlib` :pip install pathlib #pathlib中的Path类可以创建path路径对象, 属于比os.path更高抽象级别的对象
   
### 2）使用场合:
   1. 脚本同时兼容Python2和Python3 


## 23、协程的使用
### 1） 基本用法
   1. Python中的协程和生成器很相似但又稍有不同。主要区别在于： 生成器是数据的生产者 协程则是数据的消费者
   2. 使用yield便可获得了一个协程。协程会消费掉发送给它的值。用yield接收send()发送的值，用next()发放启动协程，用close()方法关闭一个协程

   ```python
    def test_demo1(pattern):
        print("Searching For {}".format(pattern))
        while True:
            line = (yield)
            if pattern in line:
                print("Find Res: {}".format(line))
    def main():
        search = test_demo1('coroutine')
        next(search)                #通过next()方法来响应send()方法。因此，你必须通过next()方法来执行yield表达式,即启动生成器
        search.send("I love you")   #我们可以通过send()方法向它传值,发送的值会被yield接收，进行函数间切换
        search.send("Don't you love me?")
        search.send("I love coroutine instead!")
        print(search)               #<generator object test_demo1 at 0x1009fcd68> 显示是一个生成器
        search.close()              #通过close()方法来关闭一个协程

```

   ```python
    import time
    #生产者消费者模型
    def consumer():
        r = ''
        while True:
            n = yield r
            if not n:
                return
            print('[CONSUMER] Consuming %s...' % n)
            time.sleep(1)
            r = '200 OK'

    def produce(c):
        next(c)     #通过next()启动生成器,python 2 可以使用c.next() 但是python3 只能使用next(c)
        n = 0
        while n < 5:
            n = n + 1
            print('[PRODUCER] Producing %s...' % n)
            r = c.send(n)   #切换到consumer中执行
            print('[PRODUCER] Consumer return: %s' % r)
        c.close()

    if __name__=='__main__':#整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
        c = consumer()
        produce(c)

```

### 2）使用场合:
   1. 协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显
   2. 不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多
   3. 协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
   4. 多线程就是协程的一种特例

## 24、function caching函数缓存
### 1） 基本用法
   1. 函数缓存允许我们将一个函数对于给定参数的返回值缓存起来，在Python 3.2版本以前我们只有写一个自定义的实现。在Python 3.2以后版本，有个`lru_cache`的装饰器，允许我们将一个函数的返回值快速地缓存或取消缓存。

   ```python
    #针对python 3.2以后的版本，采用lru_cache实现
    from functools import lru_cache
    @lru_cache(maxsize=32)  #maxsize参数是告诉lru_cache，最多缓存最近多少个返回值
    def test_demo1(n):
        if n<2:
            return n
        return test_demo1(n-1) + test_demo1(n-2)

    def test_demo2():
        pass

    def main():
        print(test_demo1(100))
        test_demo1.cache_clear()  #对返回值进行清空
        print(test_demo1)
        test_demo2()
        test_demo1.cache_clear()  #对返回值进行清空
        print(test_demo2)
```

   ```python
    #通过装饰器，自己来实现,可以创建任意类型的缓存机制。
    from functools import wraps

    def my_lru_cache(function):
        memo = {}
        @wraps(function)
        def wrapped_function(*args,**kwargs):
            if args in memo:
                return memo[args]
            else:
                rv = function(*args,**kwargs)
                memo[args] = rv
                return rv
        return wrapped_function

    @my_lru_cache
    def test_demo1(n):
        if n<2:
            return n
        return test_demo1(n-1) + test_demo1(n-2)

    def test_demo2():
        pass

    def main():
        print(test_demo1(100))
        print(test_demo1)
        test_demo2()
        print(test_demo2)
```

### 2）使用场合:
   1. 当一个I/O密集的函数被频繁使用相同的参数调用的时候，函数缓存可以节约时间



## 25、Context managers 上下文管理器
### 1） 基本用法
   1. 上下文管理器最广泛的案例就是with语句了，with open(file_name, 'w') as fd:下面的代码是等效的

   ```python
   #通过使用with，许多样板代码(boilerplate code)被消掉了。 这就是with语句的主要优势，它确保我们的文件会被关闭，而不用关注嵌套代码如何退出
    def test_demo1():
        with open('test1.log', 'w') as fd:
            # raise Exception("test")  #测试1， 创建文件，不写入内容
            fd.write('hello world!')
            # raise Exception("test2")  #测试2， 创建文件，写入内容


    def test_demo2():
        fd = open("test2.log",'w')
        try:
            # raise Exception("test")  ##测试1， 创建文件，不写入内容
            fd.write('hello world!')
            raise Exception("test2")  #测试2， 创建文件，写入内容
        finally:
            fd.close()
```

   2. 一个上下文管理器的类，最起码要定义__enter__和__exit__方法,对照下面的代码，看看底层都发生了什么。
   -. with语句先暂存了File类的__exit__方法,然后它调用File类的__enter__方法
   -. __enter__方法打开文件并返回给with语句,打开的文件句柄被传递给opened_file参数
   -. 我们使用.write()来写文件完成后,with语句调用之前暂存的__exit__方法
   -. __exit__方法关闭了文件,__exit__方法的这三个参数：type, value和traceback。
   -. 如果发生异常，Python会将异常的type,value和traceback传递给__exit__方法,它让__exit__方法来处理异常
   -. 如果__exit__返回的是True，那么这个异常就被优雅地处理了。如果__exit__返回的是True以外的任何东西，那么这个异常将被with语句抛出

   ```python
    class MyFileClass(object):
        def __init__(self,file_name,method):
            self.__dict__.update({k:v for k,v in locals().items() if k !='self'})
            self._fd = open(self.file_name,self.method)

        def __enter__(self):
            return self._fd

        def __exit__(self, exc_type, exc_val, exc_tb):
            self._fd.close()
            return True  #返回True，表明这个中间出现的异常已经被优雅的处理掉了，如果返回其他（非True）,异常则会被with 抛出到上一层

    def test_demo3():
        with MyFileClass('test3.log','w') as fd:
            # raise Exception("test")  ##测试1， 创建文件，不写入内容
            fd.write("hello world!")
            raise Exception("test2")  #测试2， 创建文件，写入内容

```

   3. 通过装饰器（decorators） 和 生成器 （generators）来实现上下文管理器。python 有专门的contextlib模块，用来生成一个上下文管理器，而不是使用类。

   ```python
    from contextlib import contextmanager

    @contextmanager
    def test_demo1(file_name,mode):
        f = open(file_name,mode)
        yield f
        f.close()

    def main():
        with test_demo1('test2_1.log', 'w') as fd:
            fd.write("hello world!")

```


### 2）使用场合:
   1. 上下文管理器允许你在有需要的时候，精确地分配和释放资源
   2. 上下文管理器的常见用例，是资源的加锁和解锁，以及关闭已打开的文件

