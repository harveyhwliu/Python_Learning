#!/usr/bin/python
#coding:utf-8
import traceback
import os
import time
#可以通过导入requests包来作为网络库
import requests

#导入reuqest网络库
try:
    import urllib.request as urllib_request     # for Python 3
    from urllib.request import urlretrieve
except ImportError:
    import urllib2 as urllib_request            # for Python 2
    from urllib import urlretrieve

#导入beautifulsoup
from bs4 import BeautifulSoup as bf

import random

from openpyxl import Workbook


def insert(conn, info):
   '''数据写入数据库'''
   with conn.cursor() as cursor:
       sql = "INSERT INTO `python` (`shortname`, `fullname`, `industryfield`, `companySize`, `salary`, `city`, `education`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
       cursor.execute(sql, info)
   conn.commit()


def get_html_content(url, page, lang_name):
    """
    获取  页面信息
    :param url:
    :param page:  页码
    :param lang_name:  编程语言的名称
    :return:
    """
    headers = {#模仿浏览器，设置请求首部
        'Host': 'www.lagou.com',
       'Connection': 'keep-alive',
       'Content-Length': '25',
       'Origin': 'https://www.lagou.com',  #这里网页请求没有这个请求首部
       'X-Anit-Forge-Code': '0',
       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
       'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
       'Accept': 'application/json, text/javascript, */*; q=0.01',
       'X-Requested-With': 'XMLHttpRequest',
       'X-Anit-Forge-Token': 'None',
       'Referer': 'https://www.lagou.com/jobs/list_Python/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=',
       'Accept-Encoding': 'gzip, deflate, br',
       'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
    }
    post_params = {'first': 'false', 'pn': page, 'kd': lang_name}
    json = requests.post(url,post_params, headers=headers).json()
    list_con = json['content']['positionResult']['result']
    info_list = []
    for i in list_con:
       info = []
       info.append(i.get('companyShortName', '无'))
       info.append(i.get('companyFullName', '无'))
       info.append(i.get('industryField', '无'))
       info.append(i.get('companySize', '无'))
       info.append(i.get('salary', '无'))
       info.append(i.get('city', '无'))
       info.append(i.get('education', '无'))
       info_list.append(info)
    return info_list

def main():
    try:
        lang_name = 'python'
        wb = Workbook()  # 打开 excel 工作簿
        for i in ['北京', '上海', '广州', '深圳', '杭州']:   # 五个城市
           page = 1
           ws1 = wb.active
           ws1.title = lang_name
           url = 'https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false'.format(i)
           while page < 31:   # 每个城市30页信息
               info = get_html_content(url, page, lang_name)
               page += 1
               time.sleep(random.randint(10, 20))
               for row in info:
                   ws1.append(row)
        wb.save('{}职位信息.xlsx'.format(lang_name))
    except Exception as e:
        errorMsg = '爬取失败，异常{},{}'.format(str(e),traceback.format_exc())
        print(errorMsg)

if __name__ == "__main__":
    main()
