#coding:utf-8
import urllib2
import json

from city import city
#cityname = raw_input('输入城市名称:')
cityname="长春"
citycode = city.get(cityname)
if citycode:
    url=("http://www.weather.com.cn/data/cityinfo/%s.html") % citycode
    content = urllib2.urlopen(url).read()
    records = json.loads(content)
else:
    content="error name"
print content
print records
print type(content)
print type(records)
result = records['weatherinfo']
print result
strTemp='%s~%s %s'%(result['temp1'],result['temp2'],result['weather'])
print strTemp