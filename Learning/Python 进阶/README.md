### 0、重要的Python 库
   0. 推荐大家使用豆瓣的源
      1. pip install matplotlib==2.2.4  -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
      2. pip install numpy -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
      3. pip install pandas  -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
      4. pip install seaborn scipy==1.2.0  -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

   1. Numpy (Numerical python) python 科学计算的基础包
      1. python -m pip list 查看 
      2. python -m pip install --upgrade pip 更新 
      3. python -m pip install numpy 安装  （使用豆瓣的源）
     
   2. Pandas 快速处理结构化数据的大量数据结构和函数  + DataFrame
      1. 安装前，需要安装Cython或者升级Cython先   pip install Cython
      
   3. Matplotlib 最流行的绘图数据图表的python库
   4. Scipy  包括统计,优化,整合,线性代数模块,傅里叶变换,信号和图像处理,常微分方程求解器等等

### 1、 python 2 和 python 3 的区别
   1. https://wiki.python.org/moin/Python2orPython3
   2. https://www.cnblogs.com/weikunzz/p/6857971.html
   3. https://blog.csdn.net/weixin_41819299/article/details/81259721
   4. filter map 函数Python2返回的是可迭代对象Iteratable，而Python3 返回的迭代器Iterator,需要通过list()来转一下,且python3 需要通过from functools import reduce 导入reduce,python2 则不需要的
   5. type返回结果的类型有区别了，例如 type("ss") ，python2 返回结果是<type 'str'>,python3 返回结果是<class 'str'>
   6. python3取消了python2中dict的if _dict_obj.has_key(key)的方法，python3中使用if key in _dict_obj:

### 2、*args 和 **kwargs的区别
## 1） 基本用法
   1. 用来给函数传参，标准参数与*args、**kwargs在使用时的顺序为：some_func(fargs1，...fargsn, *args, **kwargs)
   2. *args 和 **kwargs 不是关键字，可以替换成成其他合法变量名
   3. *args 是一个list，可以采用some_func(*args)传递参数，但是这个list的长度必须大于等于some_func的标准形参个数，多余的参数放到函数args中
   4. *kwargs是一个dict,可以采用some_func(**kwargs)传递参数，但这个dict的key必须全部包括some_func形参的名，否则会报错，多余的部分放到函数kwargs这个dict中
## 2）使用场合
   1. 不知道用户传递的参数有多少
   2. monkey patching,只是在程序运行时(runtime)修改某些代码。 打个比方，你有一个类，里面有个叫get_info的函数会调用一个API并返回相应的数据。如果我们想测试它，可以把API调用替换成一些测试数据obj.func = _nws_func
   3. 最常见的用例是在写函数装饰器的时候
   
### 3、 调试代码 pdb
## 1） 基本用法
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

## 2）使用场合
   1. 一种交互的源代码调试功能，主要特性包括设置断点、单步调试、进入函数调试、查看当前代码、查看栈片段、动态改变变量的值等 

### 4、 Generators 生成器
## 1） 基本用法
   1. 可迭代对象(Iterable) 比如list,str 就是能提供迭代器的任意对象，Python中任意的对象，只要它定义了可以返回一个迭代器的__iter__方法，或者定义了可以支持下标索引的__getitem__方法，就是可迭代对象。  
   2. 迭代器(Iterator),任意对象，只要定义了next(Python2) 或者__next__方法，它就是一个迭代器。
   3. 迭代(Iteration)，简单说，就是从某个地方（比如一个列表）取出一个元素的过程。当我们使用一个循环来遍历某个东西时，这个过程本身就叫迭代。
   4. 生成器(Generators) 也是一种迭代器，但是你只能对其迭代一次。这是因为它们并没有把所有的值存在内存中，而是在运行时生成值。你通过遍历来使用它们，要么用一个“for”循环，要么将它们传递给任意可以进行迭代的函数和结构。大多数时候生成器是以函数来实现的。然而，它们并不返回一个值，而是yield(暂且译作“生出”)一个值
   5. 通过yield返回一个generator 对象，运行时才生成结果值
   6. Python内置函数：next()。它允许我们获取一个Iterator的下一个元素，实际上是yield返回所有元素后，再次调用 next()触发了一个StopIteration的异常，for循环会自动捕捉到这个异常并停止调用next()。
   7. Python内置函数，iter。它将根据一个可迭代对象返回一个迭代器对象,比如print next(iter([1,2,3]))
   
## 2）使用场合
   1. 节省内存，生成器最佳应用场景是：你不想同一时间将所有计算出来的大量结果集分配到内存当中，特别是结果集里还包含循环。

### 5、 MAP Filter reduce
## 1） 基本用法
   1. Map会将一个函数映射到一个输入列表的所有元素上。这是它的规范：map(function_to_apply, list_of_inputs),举例：list(map(lambda x: x**2, [1,2,3,4,5]))
   2. filter过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表，符合要求即函数映射到该元素时返回值为True,filter(lambda x:x>0,[0,1,2,3])
   3. 当需要对一个列表进行一些计算并返回结果时，Reduce 是个非常有用的函数,举例：reduce(lambda x,y:x+y,[1,2,3,4,5,6,7,8,9])#求列表的各项元素之和


## 2）使用场合
   1. 简化代码，提高效率，例如对list的处理上取代for循环

### 6、 set的使用
## 1） 基本用法
   1. set不能包含重复的值,例如对查找重复的元素：print(list(set([x for x in [1,2,3,2] if [1,2,3,2].count(x)>1])))
   2. set用来求两个序列的交集：print(set(a).intersection(set(b)))
   3. set用来求两个序列中不交叉的数据集：print(set(a).difference(set(b)))  #在a序列但不在b序列中的元素集


## 2）使用场合
   1. 通过set不能包含重复元素的特性，实现业务侧查重、查交集、查差集的需求

### 7、python中的三元运算符
## 1） 基本用法
   1. 三元运算符是基于条件表达式真假的条件判断，python2.4以上才支持，举例：x=0 if x in pid_l else pid_l[x]
   2. 切记使用print((1/0,11)[condition]) 这种元组条件表达式，因为元素是先建立数据，再利用下标索引来查找数据，因此在元组中所有条件都执行

## 2）使用场合
   1. 省略多余的if表达式，可以使代码简单可维护
   2. 如果逻辑中的条件异常，或者是重计算型（计算较久）的情况下，最好尽量避免使用元组条件表达式

### 8、decorators 装饰器
## 1） 基本用法
   1. decorators 是修改其他函数的功能的函数。他们有助于让在对已有函数进行功能扩充，也更Pythonic（Python范儿）
   2. 可以在函数中定义另外的函数。也就是说：我们可以创建嵌套的函数,并可以在外层函数中返回其内内嵌函数；函数也可以作为实参传递给另外函数的形参例如printNum(getNum)，这里getNum是一个函数
   3. 直接采用函数内嵌的方式返回，发现采用注解前后，本质上是函数的名字和注释文档docstring已经发生了重写。使用from functools import wraps 中@wraps(func)  @wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。

## 2）使用场合
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
### 9、
## 1） 基本用法
   1.

## 2）使用场合
   1.








