#coding:utf-8
class url_manager:
    def __init__(self):
        self.basisUrl = 'http://baike.baidu.com'
        self.rootUrl = '/view/21087.htm'
        self.oldUrls = []
        self.newUrls = []
        pass
    def getRootUrl(self):
        url = self.basisUrl + self.rootUrl
        if url not in self.oldUrls:
            self.oldUrls.append(url)
        return url

    def getOldUrls(self):
        return self.oldUrls
    def getNewUrls(self):
        return self.newUrls
    def inputNewUrl(self, newUrls):
        if(isinstance(newUrls, list)):
            for new_url in newUrls:
                fullurl = self.basisUrl + new_url
                if fullurl not in self.oldUrls and fullurl not in self.newUrls:
                    self.newUrls.append(fullurl)
        elif(isinstance(newUrls, str)):
            fullurl = self.basisUrl + newUrls
            if fullurl not in self.oldUrls and fullurl not in self.newUrls:
                self.newUrls.append(fullurl)

    def getNewUrl(self):
        newUrl = self.newUrls.pop(0)
        if newUrl not in self.oldUrls:
            self.oldUrls.append(newUrl)
        return newUrl