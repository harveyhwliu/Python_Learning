#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')
import  inspect

class demo1(object):
    def __init__(self,name=1,id=1):
        self.name = name
        self.id   = id

class demo2(object):
    __slots__ = ['name','id']       #使用__slots__  告诉Python不要使用字典，而且只给一个固定集合的属性分配空间,没有__dict__对象了
    def __init__(self,name=1,id=1):
        self.name = name
        self.id   = id

def test_demo1():
    a=12
    print(dir([1,2,3]))
    print(dir(demo1()))
    print(dir(demo2()))
    print(dir())

def test_demo2():
    print(inspect.getmembers(demo1()))
    print(inspect.getmembers(demo2()))  #发现 使用__slot__ 后对象少了__dict__ 属性

def main():
    # test_demo1()
    test_demo2()

if __name__ == "__main__":
    main()

