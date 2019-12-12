#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')
import  time

def test_demo1(pattern):
    print("Searching For {}".format(pattern))
    while True:
        line = (yield)
        if pattern in line:
            print("Find Res: {}".format(line))

#生产者消费者模型
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    next(c)     #通过next()启动生成器,python 2 可以使用c.next() 但是python3 只能使用next(c)
    n = 0
    while n < 10000:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)   #切换到consumer中执行
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

def test_demo2():
    c = consumer()
    produce(c)

def main():
    # search = test_demo1('coroutine')
    # next(search)                #通过next()方法来响应send()方法。因此，你必须通过next()方法来执行yield表达式
    # search.send("I love you")   #我们可以通过send()方法向它传值,发送的值会被yield接收
    # search.send("Don't you love me?")
    # search.send("I love coroutine instead!")
    # print(search)               #<generator object test_demo1 at 0x1009fcd68> 显示是一个生成器
    # search.close()              #通过close()方法来关闭一个协程
    test_demo2()

if __name__ == "__main__":
    main()

