#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')

#针对python 3.2以后的版本，采用lru_cache实现
from functools import lru_cache
@lru_cache(maxsize=32)  #maxsize参数是告诉lru_cache，最多缓存最近多少个返回值
def test_demo1(n):
    if n<2:
        return n
    return test_demo1(n-1) + test_demo1(n-2)

def test_demo2():
    pass

def main():
    print(test_demo1(100))
    test_demo1.cache_clear()  #对返回值进行清空
    print(test_demo1)
    test_demo2()
    test_demo1.cache_clear()  #对返回值进行清空
    print(test_demo2)

if __name__ == "__main__":
    main()

