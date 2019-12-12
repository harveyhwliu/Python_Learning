#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')

def test_demo1():
    with open('test1.log', 'w') as fd:
        # raise Exception("test")  #测试1， 创建文件，不写入内容
        fd.write('hello world!')
        # raise Exception("test2")  #测试2， 创建文件，写入内容


def test_demo2():
    fd = open("test2.log",'w')
    try:
        # raise Exception("test")  ##测试1， 创建文件，不写入内容
        fd.write('hello world!')
        # raise Exception("test2")  #测试2， 创建文件，写入内容
    finally:
        fd.close()

class MyFileClass(object):
    def __init__(self,file_name,method):
        self.__dict__.update({k:v for k,v in locals().items() if k !='self'})
        self._fd = open(self.file_name,self.method)

    def __enter__(self):
        return self._fd

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._fd.close()
        print("Exception has been handled")
        return True  #返回True，表明这个中间出现的异常已经被优雅的处理掉了，如果返回其他（非True）,异常则会被with 抛出到上一层

def test_demo3():
    with MyFileClass('test3.log','w') as fd:
        raise Exception("test")  ##测试1， 创建文件，不写入内容
        fd.write("hello world!")
        # raise Exception("test2")  #测试2， 创建文件，写入内容

def main():
    test_demo1()
    test_demo2()
    test_demo3()

if __name__ == "__main__":
    main()

