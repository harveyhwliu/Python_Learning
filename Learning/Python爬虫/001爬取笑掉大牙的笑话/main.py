#!/usr/bin/python
#coding:utf-8
import traceback
import os
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

def get_content(html,page):
    """
    获取第几页的内容
    :param html:
    :param page:
    :return:
    """
    output = """第{}页 标题:{} 时间{} \n\n{}\n\n------------\n\n\n"""  # 最终输出格式
    html_parser = bf((html.replace("<br>","")).replace("<br/>","\n"), 'html.parser') #替换掉br的问题
    try:
        content_title = html_parser.head.title.text
    except Exception  as e :
        errorMsg = "get page {0} failed for {1}".format(page,e)
        print(errorMsg)
        return
    con = html_parser.find(id='main')
    con_list = con.find_all('div', class_="content")    #找到笑话信息
    all_content_l = []
    for i in con_list:
        _title = i.find('h2').string                    #标题
        _time_info = i.find('span').string              #时间和多少人阅
        content_all_info_l = i.text.split(_time_info)
        try:
            if len(content_all_info_l) >=2 and content_all_info_l[1]:
                _res = output.format(page,_title.encode("utf8"),
                                                   _time_info.encode("utf8"),
                                                   content_all_info_l[1].encode("utf8"))
                all_content_l.append(output.format(page,_title.encode("utf8"),
                                                   _time_info.encode("utf8"),
                                                   content_all_info_l[1].encode("utf8")))
        except Exception as e:
            errorMsg = "get page {0} failed for {1}".format(page,e)
            print(errorMsg)
    if all_content_l:
        save_file(content_title.encode("utf8"),*all_content_l)


def download_page(url):
    """
    下载URL内容
    :param url:
    :return:
    """
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)  # 增加headers, 模拟浏览器
    return r.text

def save_file(content_title,*args):
    """
    将文件内容保存到本地文件中
    :param args:
    :return:
    """
    _path = "./txt/"
    if not os.path.exists(_path):
        os.mkdir(_path)
    _file_name = "{0}{1}.txt".format(_path,content_title)
    for i in args:
        with open(_file_name, 'w') as fd:
            fd.write(i)

def main():
    try:
        #笑话大全  基本的URL构成
        for i in range(95, 5000):   #这里选择的没有依据，就是根据发现的规律95之后又数据，太大会提示找不到
            url = 'http://xiaodiaodaya.cn/article/view.aspx?id={}'.format(i)
            html = download_page(url)
            get_content(html, i)
    except Exception as e:
        errorMsg = '爬取失败，异常{},{}'.format(str(e),traceback.format_exc())
        print(errorMsg)

if __name__ == "__main__":
    main()
