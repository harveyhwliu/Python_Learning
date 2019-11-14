#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')
from functools import wraps
import time

def test_mutable_demo1():#list dict 是mutable 类型
    a=["hello"]
    a+=["world"]
    a+="ok"
    print(id(a))
    print(a)
    print(id(a))
    print(a)
    print(id(a))

def test_immutable_demo2():#string tuple int float都是immutable 类型变量
    a="hello"
    print(id(a))
    print(a)
    a+="ok"
    print(id(a))
    print(a)


def main():
    # test_mutable_demo1()
    test_immutable_demo2()

if __name__ == "__main__":
    main()

