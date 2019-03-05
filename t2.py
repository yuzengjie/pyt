import urllib

from urllib import request

if __name__=='__main__':
    url = 'http://jobs.zhaopin.com/bj1400001/'
    rsp = urllib.request.urlopen(url)

    print(type(rsp))
    print(rsp)

    print("url:{0}".format(rsp.geturl()))
    print("info:{0}".format(rsp.info))
    print("code:{0}".format(rsp.getcode()))
    html = rsp.read()

    html = html.decode()

