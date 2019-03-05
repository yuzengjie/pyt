'''
利用parse模块模拟post请求
分析百度词典
分析步骤：
1.打开f12
2.尝试输入单词girl，发现每敲一个字母后都有请求
3.请求地址是 http：//fanyi.baidu.com/sug
4.利用NetWork-All-Hearders,查看，发现Form的值是 kw：girl
5.检查返回内容格式，发现返回的是json格式内容==>需要用到json包
'''

from urllib import request,parse
import json

baseurl ='https://fanyi.baidu.com/sug'

data = {
    'kw':'girl'
}

data = parse.urlencode(data).encode()

print(type(data))

headers = {
    
    'Content-Length':len(data)
}

rsp = request.urlopen(baseurl,data=data)

json_data = rsp.read().decode('utf-8')
print(type(json_data))
print(json_data)

json_data = json.loads(json_data)
print(type(json_data))
print(json_data)