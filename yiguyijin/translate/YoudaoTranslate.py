# -*- coding: utf-8 -*-
import json
import urllib2
import sys
class YoudaoTranslate:
    baseurl = 'http://fanyi.youdao.com/openapi.do?keyfrom=yiguyijin&key=958977855&only=translate&type=data&doctype=json&version=1.1&q='
    def __init__(self,word):
        self.qword = word
        self.__getTranslateInfo()
    def __getTranslateInfo(self):
        if type(self.qword).__name__ == "unicode":
            print '是unicode编码格式'
            self.qword = self.qword.encode('UTF-8')
        url = self.baseurl+ urllib2.quote(self.qword)
        resp = urllib2.urlopen(url).read()
        self.afterTranslateWord = json.loads(resp)
    def printTranslateInfo(self):
        print '翻译结果：'
        print self.afterTranslateWord
    def getTranslateResult(self):
        if(self.afterTranslateWord['errorCode'] == 0):
            resultList = self.afterTranslateWord['translation']
            strResult = self.afterTranslateWord['query']
            strResult += u'\n'
            for i in range(len(resultList)):
                strResult += resultList[i]
                if(i+1 < len(resultList)):
                    strResult += ','
            return strResult
        else:
            return u'没有找到相关词汇'

if __name__ == "__main__":
    import chardet
    word1 = u'试一试'
    #print chardet.detect(word1)
    str = word1
    print str
    #str.decode('utf-8')
    #print chardet.detect(str)
    testTranslate = YoudaoTranslate(str)
    testTranslate.printTranslateInfo()
    print testTranslate.getTranslateResult()