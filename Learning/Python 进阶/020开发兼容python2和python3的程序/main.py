#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')
from __future__ import with_statement
from __future__ import print_function
from future.builtins.disabled import *



def test_demo1():
    print(print)

def test_demo2():
    try:
        import urllib.request as urllib_request     # for Python 3
    except ImportError:
        import urllib2 as urllib_request            # for Python 2

    print(urllib_request.localhost())

def test_demo3():
    pass


def main():
    test_demo1()
    test_demo2()
    test_demo3()

if __name__ == "__main__":
    main()

