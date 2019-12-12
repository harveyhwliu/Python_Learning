#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')
def test_demo1():
    import io

    with open('th.jpeg', 'rb') as inf:
        jpgdata = inf.read()

    if jpgdata.startswith(b'\xff\xd8'):
        text = u'This is a JPEG file (%d bytes long)\n'
    else:
        text = u'This is a random file (%d bytes long)\n'

    with io.open('summary.txt', 'w', encoding='utf-8') as outf:
        outf.write(text % len(jpgdata))


def main():
    test_demo1()

if __name__ == "__main__":
    main()

