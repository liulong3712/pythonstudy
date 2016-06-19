from bs4 import BeautifulSoup
import urllib2
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""


soup = BeautifulSoup(html)
#soup = BeautifulSoup(open('index.html'))
#print soup.prettify()
print soup.title
print soup.head
print soup.a
print type(soup.a)
print soup.name
print soup.head.name
print soup.a.attrs
print soup.a['class']
print soup.a.get('class')
print soup.a.string
print type(soup.p.string)
print type(soup.a.string)
print soup.string
for mystring in soup.stripped_strings:
    print repr(mystring)
for sibling in soup.a.next_siblings:
    print repr(sibling)
print '--------------------------'
print soup.find_all('p')
for tag in soup.find_all(True):
    print tag.name
print '-----------------------------'
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
print soup.find_all(has_class_but_no_id)
'''
old_url = 'http://www.jiyoutang.com'
urlreponse = urllib2.urlopen(old_url).read()
print urlreponse
print '-------------------------------------------'
soup1 = BeautifulSoup(urlreponse)
print soup1.prettify()
'''