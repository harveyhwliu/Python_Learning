#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')
from contextlib import contextmanager

@contextmanager
def test_demo1(file_name,mode):
    f = open(file_name,mode)
    yield f
    f.close()

def main():
    with test_demo1('test2_1.log', 'w') as fd:
        fd.write("hello world!")

if __name__ == "__main__":
    main()

