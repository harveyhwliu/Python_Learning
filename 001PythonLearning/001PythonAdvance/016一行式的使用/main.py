#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')
from pprint import pprint
import itertools
import inspect

def test_demo1():
    my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
    pprint(my_dict)
    print(my_dict)

def test_demo2():
    a_list = [[1, 2], [3, 4], [5, 6]]
    print(list(itertools.chain.from_iterable(a_list)))
    print(list(itertools.chain(*a_list)))


class A(object):
    def __init__(self, a, b, c, d, e, f):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})

    def show(self):
        pprint(self.__dict__["a"])
        pprint(self.__dict__["b"])
        pprint(self.a)
        pprint(self.b)
        pprint("{0} {1}".format(id(self.a),id(self.__dict__["a"])))
        pprint("{0} {1} {2} {3} {4} {5}".format(self.a,self.b,self.c,self.d,self.e,self.f))

def test_demo3():
    a = A("1",12.2,"3","4","5",6)
    print(dir(a))
    print(inspect.getmembers(a))
    print(a.a)
    print(a.b)
    a.show()

def main():
    test_demo1()
    test_demo2()
    test_demo3()


if __name__ == "__main__":
    main()

