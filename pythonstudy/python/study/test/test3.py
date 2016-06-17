#coding:utf-8
import urllib2
req1 = urllib2.Request('http://bbs.csdn.net/callmewhy')
req2 = urllib2.Request('http://baibai.com')

try:
    urllib2.urlopen(req2)
except urllib2.HTTPError, e:
    print e.code
    print e.errno
    #print e.read()
except urllib2.URLError, e:
    print e.reason
else:
    print '没有找到理由'

#另一种方法
try:
    urllib2.urlopen(req1)
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print e.code
    elif hasattr(e, 'reason'):
        print e.reason
    else:
        print '没有找到理由'
