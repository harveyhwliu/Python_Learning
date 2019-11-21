#!/usr/bin/python
#coding:utf-8
import traceback
from pprint import pprint

def main():
    try:
        pass
    except Exception as e:
        errorMsg = '爬取失败，异常{},{}'.format(str(e),traceback.format_exc())
        pprint(errorMsg)

if __name__ == "__main__":
    main()