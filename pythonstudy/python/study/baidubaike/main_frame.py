#coding:utf-8
from python.study.baidubaike.result_output import result_output
from python.study.baidubaike.html_parse import html_parse
from python.study.baidubaike.html_download import html_download
from python.study.baidubaike.url_manager import url_manager

if __name__ == '__main__':
    myUrlManager = url_manager()
    print myUrlManager.getNewUrls()
    needPaseUrl = myUrlManager.getRootUrl()
    #print needPaseUrl
    #myUrlManager.inputNewUrl(needPaseUrl)
    #print myUrlManager.getNewUrls()
    getNumbers = 0;
    myHtmlDownload = html_download()
    myHtmlParse = html_parse()
    myResultOutput = result_output()
    while(True):
        htmlData = myHtmlDownload.downUrl(needPaseUrl)
        if(len(htmlData) > 0):
            (newUrls,outputData) = myHtmlParse.parseUrl(htmlData)
            #print newUrls
            print outputData
            if(not any(outputData)):
                print '解析出错：',needPaseUrl
                needPaseUrl = myUrlManager.getNewUrl()
                continue
            myResultOutput.outPutFile(outputData)
            myUrlManager.inputNewUrl(newUrls)
            needPaseUrl = myUrlManager.getNewUrl()
            print myUrlManager.getNewUrls()
            print myUrlManager.getOldUrls()
            getNumbers = getNumbers + 1
            if(getNumbers == 100):
                break
            if(not any(needPaseUrl)):
                print '获取url出错：',needPaseUrl
                continue
        needPaseUrl = myUrlManager.getNewUrl()

