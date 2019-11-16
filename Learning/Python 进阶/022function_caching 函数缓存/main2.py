#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')

#通过装饰器，自己来实现,可以创建任意类型的缓存机制。
from functools import wraps

def my_lru_cache(function):
    memo = {}
    @wraps(function)
    def wrapped_function(*args,**kwargs):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args,**kwargs)
            memo[args] = rv
            return rv
    return wrapped_function

@my_lru_cache
def test_demo1(n):
    if n<2:
        return n
    return test_demo1(n-1) + test_demo1(n-2)

def test_demo2():
    pass

def main():
    print(test_demo1(100))
    print(test_demo1)
    test_demo2()
    print(test_demo2)

if __name__ == "__main__":
    main()

