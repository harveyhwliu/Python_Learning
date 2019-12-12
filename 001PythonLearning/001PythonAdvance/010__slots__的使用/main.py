#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')
from functools import wraps
import time
import resource

class demo1(object):
    def __init__(self,name=1,id=1):
        self.name = name
        self.id   = id

class demo2(object):
    __slots__ = ['name','id']       #使用__slots__  告诉Python不要使用字典，而且只给一个固定集合的属性分配空间
    def __init__(self,name=1,id=1):
        self.name = name
        self.id   = id

def test(cls):
    mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    l = []
    for i in range(500000):
        l.append(cls())
    mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    del l
    print('Class: {}:\n'.format(getattr(cls, '__name__')))
    print('Initial RAM usage: {:14,}'.format(mem_init))
    print('  Final RAM usage: {:14,}'.format(mem_final))
    print('-' * 20)



def test_slots_demo1():#使用__slots__ 后，节省了>30%+的内存
    test(demo1)
    test(demo2)



def main():
    test_slots_demo1()

if __name__ == "__main__":
    main()

