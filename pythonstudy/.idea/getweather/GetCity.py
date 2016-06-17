#coding:utf-8
import urllib2

from GetProvince import provinces
url = 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces[5:8]:
    p_code = p.split('|')[0]
    url2 = url % p_code
    content2 = urllib2.urlopen(url2).read()
    print content2
    cities = content2.split(',')
    for xian in cities:
        x_code = xian.split('|')[0]
        url3 = url % x_code
        content3 = urllib2.urlopen(url3).read()
        print content3
