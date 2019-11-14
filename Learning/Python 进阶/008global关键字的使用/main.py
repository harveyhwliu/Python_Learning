#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')
from functools import wraps
import time

def test_demo1(a,b):
    return a+b

def test_demo2(a,b):
    global result   #不能直接赋值（初始化）
    result = a+b

def test_global_demo1():
    a=1
    b=2
    print(test_demo1(a,b))
    test_demo2(a,b)
    print(result)

def test_global_demo2():
    a=1
    b=2
    print(test_demo1(a,b))
    # test_demo2(a,b)
    print(result)    #此时由于没有执行global result ，因此产生报错global name 'result' is not defined


def main():
    test_global_demo1()
    # test_global_demo2()

if __name__ == "__main__":
    main()

