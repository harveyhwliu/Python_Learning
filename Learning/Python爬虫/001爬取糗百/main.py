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
    output = """第{}页 作者：{} 性别：{} 年龄：{} 点赞：{} 评论：{}\n{}\n------------\n"""  # 最终输出格式
    soup = bf(html, 'html.parser')
    title = soup.find()
    con = soup.find(id='content-left')  # 如图一红色方框
    con_list = con.find_all('div', class_="article")  # 找到文章列表
    for i in con_list:
        author = i.find('h2').string  # 获取作者名字
        content = i.find('div', class_='content').find('span').get_text()  # 获取内容
        stats = i.find('div', class_='stats')
        vote = stats.find('span', class_='stats-vote').find('i', class_='number').string
        comment = stats.find('span', class_='stats-comments').find('i', class_='number').string
        author_info = i.find('div', class_='articleGender')  # 获取作者 年龄，性别
        if author_info is not None:  # 非匿名用户
            class_list = author_info['class']
            if "womenIcon" in class_list:
                gender = '女'
            elif "manIcon" in class_list:
                gender = '男'
            else:
                gender = ''
            age = author_info.string  # 获取年龄
        else:  # 匿名用户
            gender = ''
            age = ''

        save_file(output.format(page, author, gender, age, vote, comment, content))


def download_page(url):
    """
    下载URL内容
    :param url:
    :return:
    """
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)  # 增加headers, 模拟浏览器
    return r.text

def save_file(*args):
    """
    将文件内容保存到本地文件中
    :param args:
    :return:
    """
    _path = "./txt/"
    if not os.path.exists(_path):
        os.mkdir(_path)
    _file_name = "{0}qiubai.txt".format(_path)
    for i in args:
        with open(_file_name, 'a', encoding='utf-8') as f:
            f.write(i)


def main():
    try:
        #笑话大全  基本的URL构成
        for i in range(1, 14):
            url = 'http://xiaodiaodaya.cn/article/view.aspx?id={}'.format(i)
            html = download_page(url)
            get_content(html, i)
    except Exception as e:
        errorMsg = '爬取失败，异常{},{}'.format(str(e),traceback.format_exc())
        print(errorMsg)

if __name__ == "__main__":
    main()