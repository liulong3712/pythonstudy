#coding:utf-8
import urllib2
url1 = 'http://m.weather.com.cn/data5/city.xml'
content1 = urllib2.urlopen(url1).read()
print content1
provinces = content1.split(',')
