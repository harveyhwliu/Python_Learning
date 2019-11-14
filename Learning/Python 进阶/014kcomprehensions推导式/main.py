#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')

def test_demo1():
    multiples = [i for i in range(30) if not i % 21]
    print(multiples)

def test_demo2():
    s={"aa":11,"bb":1212}
    print({v:k for k,v in s.items()})#python3 dict没有iteritems(),只能使用items()
    mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
    mcase_frequency = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys()}
    print(mcase_frequency)

def test_demo3():
    squared = (x**2 for x in [1, 1, 2]) #python3使用() 定义返回就是一个generator,需要使用 {}来定义
    print(squared)

def main():
    # test_demo1()
    # test_demo2()
    test_demo3()

if __name__ == "__main__":
    main()

