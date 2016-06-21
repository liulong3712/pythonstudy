# coding: utf-8
import hashlib
import web
import lxml
import time
import os
import urllib2, json
from lxml import etree
from translate.YoudaoTranslate import YoudaoTranslate

class WeixinInterface:

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        #获取输入参数
        data = web.input()
        print type(data)
        print data
        if(data.has_key('openid')):
            echostr = data.openid
        elif(data.has_key('echostr')):
            echostr = data.echostr
        else:
            echostr = 'error'
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce

        #自己的token
        token = "yiguyijin" #这里改写你在微信公众平台里输入的token
        #字典序排序
        list = [token,timestamp,nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update,list)
        hashcode = sha1.hexdigest()
        #sha1加密算法

        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr

    def POST(self):
        str_xml = web.data() #获得post来的数据
        xml = etree.fromstring(str_xml)#进行XML解析
        content=xml.find("Content").text#获得用户所输入的内容
        msgType=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text
        testTranslate = YoudaoTranslate(content)
        resultContent = u''
        resultContent += testTranslate.getTranslateResult()
        return self.render.reply_text(fromUser,toUser,int(time.time()),u"翻译结果：\n"+resultContent)

urls = (
    '/weixin', 'WeixinInterface'
)
if __name__ == "__main__":
    #web.run(urls, globals())
    app = web.application(urls, globals())
    app.run()
    '''
    import chardet
    #print chardet.detect(word1)
    content = u'试试'
    testTranslate = YoudaoTranslate(content)
    resultContent = u'翻译结果：'
    #print chardet.detect(resultContent)
    #resultContent = ""
    #resultContent += testTranslate.getTranslateResult()
    print resultContent
    '''
