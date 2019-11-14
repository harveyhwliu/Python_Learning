#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')
from pprint import pprint
import itertools
import inspect
from pprint import pprint


from ctypes import *

def test_demo1():
    adder = CDLL('./adder.so')                    #加载dll
    res_int = adder.add_int(4,5)
    print("Sum of 4 and 5 = " + str(res_int))

    adder.add_float.argtypes = (c_float, c_float) # add_float 有两个形参，都是 float 类型
    adder.add_float.restype = c_float             # add_float 返回值的类型是 float
    print("Sum of 5.5 and 4.1 = ", str(adder.add_float(5.5, 4.1)))


def test_demo2():
    #module that talks to the C code
    import addList
    l = [1,2,3,4,5]
    print("Sum of List - " + str(l) + " = " +  str(addList.add(l)))

def test_demo3():
    pass



def main():
    # test_demo1()
    test_demo2()
    test_demo3()

if __name__ == "__main__":
    main()

