#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')
from __future__ import with_statement
from __future__ import print_function
from future.builtins.disabled import *
from functools import singledispatch
from pathlib import Path
def test_demo1():
    print(print)

def test_demo2():
    try:
        import urllib.request as urllib_request     # for Python 3
    except ImportError:
        import urllib2 as urllib_request            # for Python 2

    print(urllib_request)

def test_demo3():
    apply()   #python 使用会报错，python3 报错为没有定义

@singledispatch
def show(obj):
    print (obj, type(obj), "obj")

@show.register(str)
def _(text):
    print (text, type(text), "str")

@show.register(int)
def _(n):
    print (n, type(n), "int")

def test_demo4():
    show(1)
    show("xx")
    show([1])

def test_demo5():
    path = Path(__file__)
    print("{} {} {} {}".format(path.suffix,path.stem,path.name,path.parent)) #文件的后缀，文件名不带后缀，文件的完整名带后缀  没见的上级目录

def main():
    # test_demo1()
    # test_demo2()
    # test_demo3()
    test_demo4()
    test_demo5()

if __name__ == "__main__":
    main()

