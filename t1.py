from urllib import request

if __name__=='__main__':
    url = "http://jobs.zhaopin.com/bj1400001/"
    rsp = request.urlopen(url)
    html = rsp.read()
    html = html.decode()
    print(html)