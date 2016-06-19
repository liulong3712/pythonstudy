# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib2


if __name__ == "__main__":
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    #初始化headers
    headers = { 'User-Agent' : user_agent }
    try:
        url = 'http://www.qiushibaike.com/hot/page/' + str(1)
        #构建请求的request
        request = urllib2.Request(url,headers = headers)
        #利用urlopen获取页面代码
        response = urllib2.urlopen(request)
        soup = BeautifulSoup(response)
        all_divart =soup.find_all('div',class_='article block untagged mb15')
        for onedivart in all_divart:
            #名字
            one_all_a = onedivart.find_all('a')
            print one_all_a[1].contents[1].string
            #内容
            one_all_content = onedivart.find_all('div',class_='content')
            print one_all_content[0].contents[0].strip()
            print '\n'
    except urllib2.URLError, e:
        if hasattr(e,"reason"):
            print u"连接糗事百科失败,错误原因",e.reason
