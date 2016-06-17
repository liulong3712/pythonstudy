import urllib2

req = urllib2.Request('http://www.baibai.com')

try:
    response = urllib2.urlopen(req).read()
    print response

except urllib2.URLError, e:
    print e.reason
