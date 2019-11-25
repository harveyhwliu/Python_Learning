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

#导入线程库，threading提供的Condition 条件变量  对象提供了对复杂线程同步问题的支持
import threading
import time

#条件变量Condition,对象的构造函数可以接受一个Lock/RLock对象作为参数，如果没有指定，则Condition对象会在内部自行创建一个 RLock；
condition = threading.Condition()
#生成的网页内容
global_html_content_l = []
#生产者数量
gloabl_producer_cnt = 4
#当前生产的位置
global_producer_cur_index = 95
#最大生产的索引
global_producer_max_index = 5000
#消费者数量
global_consumer_cnt = 40

#生产者，负责获取网页内容
class Producer(threading.Thread):
    '''生产者'''
    ix = [0] # 生产者实例个数
             # 闭包，必须是数组，不能直接 ix = 0
    def __init__(self, ix=0):
        threading.Thread.__init__(self)
        self.ix[0] += 1
        self.setName('生产者' + str(self.ix[0]))

    def run(self):
        global condition, global_html_content_l,global_producer_cur_index,global_producer_max_index

        while True:
            if condition.acquire():         #获取内部锁
                if global_producer_cur_index <= global_producer_max_index:
                    if len(global_html_content_l) < 2*global_consumer_cnt+1:
                        url = 'http://xiaodiaodaya.cn/article/view.aspx?id={}'.format(global_producer_cur_index)
                        global_producer_cur_index +=1
                        html_content = self.download_page(url)
                        _params = dict({"url":url,"page":global_producer_cur_index,"html_content":html_content})
                        global_html_content_l.append(_params)
                        condition.notify()  #waiting状态的线程只能通过notify方法唤
                    else:
                        infoMsg= "{0}：本次休息，当前待消费数量： {1}".format(self.getName(), len(global_html_content_l))
                        print(infoMsg)
                        condition.wait()    #生产过剩，不需要再生产了
                else:
                    infoMsg= "{0}：完成生产工作，准备退出，当前待消费数量： {1}".format(self.getName(), len(global_html_content_l))
                    print(infoMsg)
                    condition.release()         #释放锁
                    break
                condition.release()         #释放锁
                time.sleep(1)

    def download_page(self,url):
        """
        下载URL内容
        :param url:
        :return:
        """
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
        r = requests.get(url, headers=headers)  # 增加headers, 模拟浏览器
        return r.text

#消费者，负责解析网页的内容
class Consumer(threading.Thread):
    '''消费者'''
    ix = [0] # 消费者实例个数
             # 闭包，必须是数组，不能直接 ix = 0
    def __init__(self):
        threading.Thread.__init__(self)
        self.ix[0] += 1
        self.setName('消费者' + str(self.ix[0]))

    def run(self):
        global condition, global_html_content_l,global_producer_cur_index,global_producer_max_index

        while True:
            if condition.acquire():
                if global_html_content_l:
                    params = global_html_content_l.pop(0) #如果共享非空，消费数据( {"url":url,"page":global_producer_cur_index,"html_content":html_content})
                    url = params["url"]
                    page = params["page"]
                    html_content = params["html_content"]
                    self.get_content(url,html_content,page)
                    condition.notify()
                    infoMsg = "{0} :当前已消费 {1}/{2}".format(self.getName(),global_producer_cur_index,global_producer_max_index)
                    print(infoMsg)
                else:
                    if global_producer_cur_index > global_producer_max_index:
                        infoMsg= "{0}：完成消费工作，准备退出，当前待消费数量： {1}".format(self.getName(), len(global_html_content_l))
                        print(infoMsg)
                        condition.release()         #释放锁
                        break
                    condition.wait()
                condition.release()

    def get_content(self,url,html,page):
        """
        获取第几页的内容
        :param html:
        :param page:
        :return:
        """

        html_parser = bf((html.replace("<br>","")).replace("<br/>","\n"), 'html.parser') #替换掉br的问题
        try:
            content_title = html_parser.head.title.text  #没有通常表示没有这个page的内容，可以忽略掉
        except Exception  as e :
            # errorMsg = "get page {0} failed for {1},the origin url is {2}".format(page,e,url)
            # print(errorMsg)
            return
        output = """第{}页 标题:{} 时间{} \n\n{}\n\n------------\n\n\n"""  # 最终输出格式
        all_content_l = []
        _image_d = {}
        all_content_l.append("""原始页面:{0}\n""".format(url))
        con = html_parser.find(id='main')
        con_list = con.find_all('div', class_="content")    #找到笑话信息
        if not con_list:
            errorMsg = "get page {0} failed for {1},the url is {2}".format(page,"html_content is None",url)
            print(errorMsg)
            return
        image_list = con.find_all('img')    #找到笑话动图
        for _img in  image_list:
            try:#针对图片
                img_url = _img.get('src')
                if img_url:
                    _img_info_l = img_url.split("/")
                    _image_name = _img_info_l[-1]
                    _image_d[_image_name] = img_url
            except Exception as e:
                errorMsg = "get page {0} image failed for {1},the url is {2}" \
                           "".format(page,e,url)
                print(errorMsg)

        _title = ""
        _time_info = ""
        for _index,i in enumerate(con_list):
            try:
                try:
                    _title = i.find('h2').text                    #标题
                    _time_info = i.find('span').text              #时间和多少人阅
                except:
                    pass
                content_all_info_l = i.text.split(_time_info)

                if len(content_all_info_l) >=2 and content_all_info_l[1]:
                    _res = output.format(page,_title.encode("utf8"),
                                                       _time_info.encode("utf8"),
                                                       content_all_info_l[1].encode("utf8"))
                    all_content_l.append(output.format(page,_title.encode("utf8"),
                                                       _time_info.encode("utf8"),
                                                       content_all_info_l[1].encode("utf8")))
            except Exception as e:
                errorMsg = "get page {0} failed for {1},the url is {2}".format(page,e,url)
                print(errorMsg)
        if all_content_l and len(all_content_l)>1:
            self.save_file(url,content_title.encode("utf8"),all_content_l,type_kind=0)
        if _image_d:
            self.save_file(url,content_title.encode("utf8"),_image_d,type_kind=1)

    def save_file(self,url,content_title,content_l,type_kind = 0):
        """
        将文件内容保存到本地文件中
        :param content_l:
        :return:
        """
        image_url = ""
        try:
            if 0 == type_kind:#保存文本内容
                _path = "./txt/"
                if not os.path.exists(_path):
                    os.mkdir(_path)
                _file_name = "{0}{1}.txt".format(_path,content_title)
                for i in content_l:
                    with open(_file_name, 'w') as fd:
                        fd.write(i)
            elif 1==type_kind:#保存图片
                _path = "./img/"
                if not os.path.exists(_path):
                    os.mkdir(_path)
                for image_name,image_url in content_l.iteritems():
                    urlretrieve(image_url,"{0}{1}{2}".format(_path,content_title,image_name))##下载图片
        except Exception as e:
            errorMsg = "record content failed for {0},the url is {1}, image_url is {2}" \
                       "".format(e,url,image_url)
            print(errorMsg)

def main():
    start_time = time.time()
    _thread_l = []
    try:
        for i in range(gloabl_producer_cnt):
            producer = Producer()
            producer.start()
            _thread_l.append(producer)
        for i in range(global_consumer_cnt):
            consumer = Consumer()
            consumer.start()
            _thread_l.append(consumer)
        for _tid in _thread_l:
            _tid.join()
    except Exception as e:
        errorMsg = '爬取失败，异常{},{}'.format(str(e),traceback.format_exc())
        print(errorMsg)
    finally:
        infoMsg = "爬虫工作完成，一共耗时%.3fs"%(time.time() - start_time)
        print(infoMsg)

if __name__ == "__main__":
    main()
