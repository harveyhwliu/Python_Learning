#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def test_generator_demo1(NUM=10):
    for i in range(NUM):
        yield i #生成器，运行时才生成值，返回结果是一个生成器generator  遇到yield 就返回，后面的不在继续执行

def test_demo1():
    n = test_generator_demo1()
    print n  # <generator object test_generator_demo1 at 0x104513d20>
    for x in n:
        print x

def test_fibon(n):
    a=b=1
    for x in range(n):
        yield a         #遇到yield就返回
        a,b = b,a+b

def test_demo2():
    for x in test_fibon(10000): #更加的节省内存
        print x


def test_generator_demo3():
    n = test_generator_demo1()
    try:
        print (next(n))
        print (next(n))
        print (next(n))
        print (next(n))
        print (next(n))
        print (next(n))
        print (next(n))
        print (next(n))
        print (next(n))
        print (next(n))
        print next(n)
    except StopIteration:  #yield 返回所有的元素后，再次调用就会抛出StopIteration的异常，for循环就是捕获这个异常并正常退出的
        pass

def test_generotor_demo4():
    str = "ssssssss"
    # print next(str)  #字符串不是一个iterator 可迭代对象不是一个可迭代器
    print next(iter(str))   #Python内置函数，iter。它将根据一个可迭代对象返回一个迭代器对象
    print next(iter([1,2,3,34,5]))

def main():
    # test_demo1(
    # test_demo2()
    # test_generator_demo3()
    test_generotor_demo4()

if __name__ == "__main__":
    main()

