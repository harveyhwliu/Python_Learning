#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pdb

def test_args_kwargs( param1,param2,param3,*argsss,**kwargssss):
    pdb.set_trace()
    infoMsg = "{0},{1},{2},{3},{4}".format(param1,param2,param3,argsss,kwargssss)
    print infoMsg

def main():
    test_args_kwargs(1,2,3,"ssss",{"hello":0,"world":1})   #打印结果：1,2,3,('ssss', {'world': 1, 'hello': 0}),{}


if __name__ == "__main__":
    main()

