#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')
from pprint import pprint
import itertools
import inspect
from pprint import pprint

def test_demo1(num = 0):
    for item in [1,2,3,4,5,0]:
        if num == item:
            #TODO 做一些动作
            break
    else:
        #没有找到的时候做一些动作
        pprint("没有找到元素，遍历了整个序列后退出的")

def test_demo2():
    pass



def main():
    test_demo1(12)
    test_demo2()


if __name__ == "__main__":
    main()

