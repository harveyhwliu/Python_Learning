#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
reload(sys)

def test_args_kwargs( param1,param2,param3,*argsss,**kwargssss):
    infoMsg = "{0},{1},{2},{3},{4}".format(param1,param2,param3,argsss,kwargssss)
    print infoMsg


# 用途 monkey patching
class test_obj(object):
    def test_args_kwargs(self):
        print "in test obj"


def main():
    test_args_kwargs(1,2,3,"ssss",{"hello":0,"world":1})   #打印结果：1,2,3,('ssss', {'world': 1, 'hello': 0}),{}
    test_args_kwargs(**{"param1":0,"param2":1,"param3":3,"param4":2}) #打印结果0,1,3,(),{'param4': 2},如果输入字典参数不含有形参名称，则会报错
    test_args_kwargs(*["param1",0,"param2",1,"param3",2])  #param1,0,param2,(1, 'param3', 2),{}

    obj = test_obj()
    obj.test_args_kwargs()
    obj.test_args_kwargs = test_args_kwargs
    obj.test_args_kwargs(**{"param1":0,"param2":1,"param3":3,"param4":2})



if __name__ == "__main__":
    main()

