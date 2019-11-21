#!/usr/bin/python
#coding:utf-8
import traceback
import os
#导入reuqest网络库
try:
    import urllib.request as urllib_request     # for Python 3
    from urllib.request import urlretrieve
except ImportError:
    import urllib2 as urllib_request            # for Python 2
    from urllib import urlretrieve

#导入beautifulsoup
from bs4 import BeautifulSoup as bf

def test():
    html = urllib_request.urlopen("https://www.baidu.com")
    #用beautifulSoup解析html
    obj = bf(html.read(),'html.parser')
    #打印标题
    title = obj.head.title
    print(title)
    #使用find_all 获取所有的图片信息,只提取logo图片的信息
    pic_info = obj.find_all('img',class_="index-logo-src")
    #提取logo 图片的信息：
    image_path = "./img/"
    if not os.path.exists(image_path):
        os.mkdir(image_path)
    for _index,pic in enumerate(pic_info):
        log_url="{0}{1}".format("https:",pic["src"])
        #下载图片
        urlretrieve(log_url,"{}logo{}.png".format(image_path,_index))

def main():
    try:
        test()
    except Exception as e:
        errorMsg = '爬取失败，异常{},{}'.format(str(e),traceback.format_exc())
        print(errorMsg)

if __name__ == "__main__":
    main()