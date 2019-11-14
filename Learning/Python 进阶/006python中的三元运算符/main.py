#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')

def test_demo1(params_pid=12):
    pid_info = {12:1,2323:2,0:11}
    _t_mark = 0 if not params_pid in pid_info else pid_info[params_pid]  #python3
    # _t_mark = 0 if not pid_info.has_key(params_pid) else pid_info[params_pid]  #python 2
    print(_t_mark)

def test_demo2():
    condition = True
    print(11 if condition else 1/0)

    #True等于1，而False等于0，这就相当于在元组中使用0和1来选取数据
    #一个不使用元组条件表达式的缘故是因为在元组中会把两个条件都执行，而 if-else 的条件表达式不会这样
    print((1/0,11)[condition])#ZeroDivisionError: integer division or modulo by zero
    #因为在元组中是先建数据，然后用True(1)/False(0)来索引到数据。 而if-else条件表达式遵循普通的if-else逻辑树，
    #因此，如果逻辑中的条件异常，或者是重计算型（计算较久）的情况下，最好尽量避免使用元组条件表达式。


def main():
    # test_demo1()
    test_demo2()




if __name__ == "__main__":
    main()

