## 1 requests 库介绍
   1. Requests 是学习爬虫的一大利器。是一个优雅简单的 HTTP库.
   2. 打开网页：

   ```python
    import requests
    url = 'http://xiaodiaodaya.cn/article/view.aspx?id={}'.format(0)
    r = requests.get(url) # 打开网址，一般我们会设置 请求头，来更逼真的模拟浏览器，下文有介绍
    r.text
```

## 2 Beautiful Soup 库介绍
   1. 拿到网页信息后，我们要解析页面，通常来说我们有以下几种方式来解析页面:   
   - 正则表达式:适用于简单数据的匹配，如果匹配内容较复杂，正则表达式写起来会很绕，同时页面内容稍微变化，正则就会失效. 
   - Lxml: 专门用来解析 XML 格式文件的库，该模块用 C 语言编写，解析速度很快，和正则表达式速度差不多，但是提供了 XPath 和 CSS 选择器等定位元素的方法.  
   - Beautiful Soup:这是一个 Python 实现的解析库，相比较于前两种来说，语法会更简单明了一点，文档也比较详细。唯一的一点就是运行速度比前两种方式慢几倍，当数据量非常大时相差会更多。 
   2. 安装beautifulsoup库：`pip install beautifulsoup4`

    ```python
    from bs4 import BeautifulSoup
    soup = bf((html.replace("<br>","")).replace("<br/>","\n"), 'html.parser') #替换掉br的问题
    soup.find('div') # 找到 div 标签
    soup.find_all('li') # 找到所有 li 标签
    for i in li:
        print(i.text)    #获取每个 li 标签的内容
    
```

## 3 采用生产者 消费者模型来实现
   1. 条件变量Condition,对象的构造函数threading.Condition()可以接受一个Lock/RLock对象作为参数，如果没有指定，则Condition对象会在内部自行创建一个 RLock；
   2.


