#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')

def test_demo1():
    add = lambda x, y: x + y
    print(add(3, 5))

def test_demo2():
    a = [(1, 2), (4, 1), (9, 10), (13, -3),(4,0)]
    a.sort()
    print(a)
    a.sort(key=lambda x: x[0])#按照元组的第1个元素来排序
    print(a)
    a.sort(key=lambda x: x[1])#按照元组的第2个元素来排序
    print(a)

def main():
    test_demo1()
    test_demo2()


if __name__ == "__main__":
    main()

