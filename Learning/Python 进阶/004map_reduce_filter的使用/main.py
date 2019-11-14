#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')

from functools import reduce


def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

def test_map_demo1():
    test = list(map(lambda x:x**2,[1,2,3,4,5,6,7,8]))
    print(test)
    funcs = [multiply, add]
    for i in range(5):
        value = map(lambda x: x(i), funcs)
        print(list(value))
        # 译者注：上面print时，加了list转换，是为了python2/3的兼容性
        #        在python2中map直接返回列表，但在python3中返回迭代器
        #        因此为了兼容python3, 需要list转换一下

def test_filter_demo1():
    test = filter(lambda x:x>0,[0,1,2,3,4])   #filter过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表，符合要求即函数映射到该元素时返回值为True
    print(list(test))   #在python2中filter直接返回列表，但在python3中返回迭代器,list转换一下


def test_reduce_demo1():
    res = reduce(lambda x,y:x+y,[1,2,3,4,5,6,7,8,9,10])  #python 3 中需要通过 from functools import reduce 导入reduce
    print(res)

def main():
    # test_map_demo1()
    # test_filter_demo1()
    test_reduce_demo1()

if __name__ == "__main__":
    main()

