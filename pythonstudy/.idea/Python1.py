
# -*- coding: utf-8 -*-

import urllib2
#https://www.baidu.com/s?wd=%E6%B5%8B%E8%AF%95
import chardet
if __name__ == "__main__":
    import urllib
    url = 'http://www.baidu.com/s'
    values = {'wd':'测试',
              's':'123'}
    data = urllib.urlencode(values) # 编码工作
    print data
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(url,data,headers)  # 发送请求同时传data表单
    print req.get_full_url()
    response = urllib2.urlopen(req)  #接受反馈的信息
    the_page = response.read()  #读取反馈的内容
    full_url = url + '?' + data
    print urllib2.urlopen(full_url).read()
    #print the_page
