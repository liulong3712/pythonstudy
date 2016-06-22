#coding:utf-8
from bs4 import BeautifulSoup
class html_parse:
    def __init__(self):
        pass

    @classmethod
    def parseUrl(self, htmlData):
        outputdata = ''
        newUrls = []
        try:
            soup = BeautifulSoup(htmlData, "lxml")
            #获取标题
            titleText = soup.find('dd',class_='lemmaWgt-lemmaTitle-title')
            outputdata += titleText.h1.string;
            #获取内容
            contentText = soup.find('div',class_='lemma-summary')
            outputdata += contentText.get_text()
            #获取所有链接
            allLinkUrls = soup.find_all('a',target='_blank',class_='')
            #print allLinkUrls
            for linkUrl in allLinkUrls:
                if(len(linkUrl.find_parent()) > 0 and linkUrl.find_parent().get('class') ==['para']):
                    #print linkUrl.get('href'),linkUrl.get('class')
                    newUrls.append(linkUrl.get('href'))
        except:
            print '解析异常'
        return newUrls,outputdata

    