#coding:utf-8
import urllib2


class html_download:
    def __init__(self):
        pass

    def downUrl(self, url):
        try:
            openResult = urllib2.urlopen(url)
            return openResult.read()
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print '解析出错：', e.code
            elif hasattr(e, 'reason'):
                print '解析出错：',e.reason
            else:
                print '没有找到理由'