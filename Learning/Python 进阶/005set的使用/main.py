#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')
def test_set_demo1():
    s = set([1,2,3,"ss","11",11])
    print(type(s))
    #查找重复的元素：
    print(list(set([x for x in [1,2,3,4,5,3,4,3,4,344,55,5] if [1,2,3,4,5,3,4,3,4,344,55,5].count(x)>1])))

def test_set_intersection():#求两个元素的交集
    a=[1,2,3,3,4]
    b=[3,4,4,5,6,7]
    print(set(a).intersection(set(b)))

def test_set_difference():#求两个元素的差集
    a=[1,2,3,3,4]
    b=[3,4,4,5,6,7]
    print(set(a).difference(set(b)))
    print(set(b).difference(set(a)))

def main():
    # test_set_demo1()
    # test_set_intersection()
    test_set_difference()
if __name__ == "__main__":
    main()

