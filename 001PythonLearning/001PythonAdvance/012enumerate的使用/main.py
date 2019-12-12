#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')

def test_demo1():
    my_list = ['apple', 'banana', 'grapes', 'pear']
    for c, value in enumerate(my_list, 1):  #从1开始计数，而不是0
        print(c, value)


    my_str = "wefasfasdfasgvbasfawe"
    for c, value in enumerate(my_str, 1):  #从1开始计数，而不是0
        print(c, value)


    my_list = ['apple', 'banana', 'grapes', 'pear']
    counter_list = list(enumerate(my_list, 1))#创建包含索引的元组
    print(counter_list)

    print()


def main():
    test_demo1()

if __name__ == "__main__":
    main()

