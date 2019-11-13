
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
   