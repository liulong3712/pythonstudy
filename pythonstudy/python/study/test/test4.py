from urllib2 import Request, urlopen, URLError, HTTPError


old_url = 'http://www.jiyoutang.com'
req = Request(old_url)
response = urlopen(req)
print response.info()
print 'Old url :' + old_url
print 'Real url :' + response.geturl()
