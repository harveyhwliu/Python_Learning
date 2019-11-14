#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')

from collections import defaultdict,Counter,deque,namedtuple
from enum import Enum

colors=(
    ('hi','hh'),
    ('hia','hha'),
    ('his','hhs'),
    ('hid','hhd'),
    ('hid','hhd'),
    ('hid','hhd'),
)

def test_collections_demo1():

    print("{0} : {1}".format(colors,type(colors)))
    _t_colors = defaultdict()
    print("{0} : {1}".format(_t_colors,type(_t_colors)))
    for v1,v2 in colors:
        _t_colors[v1] = v2
    print("{0} : {1}".format(_t_colors,type(_t_colors)))

def test_collections_demo2():
    favs = Counter(s for s, colour in colors)
    print(favs)
    favs = Counter(v for s, v in colors)
    print(favs)

    favs = Counter(s+v for s, v in colors)
    print(favs)

def test_collections_demo3():
    d = deque()
    d.append('1') #尾部追加
    d.append('2')
    d.append('3')

    print(len(d))
    print(d[0])
    print(d[-1])

    print(d)
    d.popleft()
    print(d)
    d.pop()     #默认从右侧（尾部）取出数据
    print(d)

    #也可以限制这个列表的大小，当超出你设定的限制时，数据会从对队列另一端被挤出去(pop)
    d = deque(maxlen=30)#现在当你插入30条数据时，最左边一端的数据将从队列中删除。#可以看成是循环队列
    for i in range(70):
        d.append(i)
        print(d)


def test_collections_demo4():
    s=(11,23,2323)
    print(s)
    x = namedtuple('prop1', 'v1 v2 v3')  #相当于定义key
    d = x(v1="xxs", v2=2, v3="dog")      #给对应的key赋值
    r = x(v1="xiaoming", v2=23, v3="people")      #给对应的key赋值
    print("{0} {1} {2}".format(d,d.v1,type(d)))
    print("{0} {1} {2}".format(r,r.v1,type(r)))
    r.v1=123 #nametuple 是不可变得  AttributeError: can't set attribute

class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9

    # 但我们并不想关心同一物种的年龄，所以我们可以使用一个别名
    kitten = 1  # (译者注：幼小的猫咪)
    puppy = 2   # (译者注：幼小的狗狗)


def test_collections_enum():
    Animal = namedtuple('Animal', 'name age type')
    perry = Animal(name="Perry", age=31, type=Species.cat)
    drogon = Animal(name="Drogon", age=4, type=Species.dragon)
    tom = Animal(name="Tom", age=75, type=Species.cat)
    charlie = Animal(name="Charlie", age=2, type=Species.kitten)

    print(charlie.type == tom.type)
    #获取cat的值
    print("{0} {1} {2}".format(Species(1),Species['cat'],Species.cat))



def main():
    # test_collections_demo1()
    # test_collections_demo2()
    # test_collections_demo3()
    # test_collections_demo4()

    test_collections_enum()

if __name__ == "__main__":
    main()

