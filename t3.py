import urllib
import chardet
from urllib import request

if __name__=='__main__':
    url = 'http://jobs.zhaopin.com/bj1400001/'
    rsp = urllib.request.urlopen(url)
    html = rsp.read()



    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    html = html.decode(cs.get("encoding","utf-8"))

    print(html)