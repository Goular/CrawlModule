import requests
import json
# import requests.packages from urllib3
import urllib3
from requests.exceptions import ReadTimeout
from requests.auth import HTTPBasicAuth
from requests.exceptions import ReadTimeout, HTTPError, RequestException, ConnectionError

# demo1 -- 实例引入
# response = requests.get('https://www.baidu.com')
# print(type(response))
# print(response.status_code)
# print(type(response.text))
# print(response.text)
# print(response.cookies)

# demo2 -- 各种请求方式
# requests.post('http://httpbin.org/post')
# requests.put('http://httpbin.org/put')
# requests.delete('http://httpbin.org/delete')
# requests.head('http://httpbin.org/get')
# requests.options('http://httpbin.org/get')

# demo3 -- 基本GET请求
# response = requests.get('http://httpbin.org/get')
# print(response.text)

# demo4 -- 带参数的GET请求 -- 1
# response = requests.get('http://httpbin.org/get?name=goular&age=26')
# print(response.text)

# demo4 -- 带参数的GET请求 -- 2
# data = {
#     'name': 'Jack',
#     'age': '25'
# }
# response = requests.get('http://httpbin.org/get', params=data)
# print(response.text)

# demo5 -- 解析json
# response = requests.get('http://httpbin.org/get')
# print(type(response.json()))
# print(response.json())
# print(type(response.text))
# print(json.loads(response.text))

# demo6 -- 获取二进制数据 --1
# response = requests.get('https://github.com/favicon.ico')
# print(type(response.text),type(response.content))
# print(response.text)  # 获取的是字符串数据
# print(response.content)  # 获取的是二进制数据

# demo6 -- 获取二进制数据 --2
# response = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico', 'wb') as f:
#     f.write(response.content)
#     f.close()

# demo7 -- 添加headers -- 400 Bad Request (这是由于缺失header所致)
# response = requests.get('https://www.zhihu.com/explore')
# print(response.text)

# demo7 -- 添加headers -- 正常访问
# headers = {
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
# }
# response = requests.get('https://www.zhihu.com/explore', headers=headers)
# print(response.text)

# demo8 -- 基本POST请求 -- 1
# data = {
#     'name': 'Germary',
#     'age': 26
# }
# response = requests.post('http://httpbin.org/post', data=data)
# print(response.text)

# demo8 -- 基本POST请求 -- 2
# data = {
#     'name': 'Goular',
#     'age': 18,
#     'class': 'A'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
# }
# response = requests.post('http://httpbin.org/post', data=data, headers=headers)
# print(response.text)

# demo9 -- response属性 -- 状态码，headers，cookies，url，history
# response = requests.get('http://www.jianshu.com')
# print(type(response.status_code), response.status_code)
# print(type(response.headers), response.headers)
# print(type(response.cookies), response.cookies)
# print(type(response.url), response.url)
# print(type(response.history), response.history)

# demo10 -- 状态码判断 --1 带英文的写法
# response = requests.get('http://www.baidu.com')
# if not response.status_code == requests.codes.ok:
#     exit()
# else:
#     print('Request Successfully')

# demo10 -- 状态码判断 --1 带数字的写法
# response = requests.get('http://www.baidu.com')
# if not response.status_code == 200:
#     exit()
# else:
#     print('Request Successfully')

# demo11 -- 文件上传
# files = {
#     'file': open('favicon.ico', 'rb')
# }
# response = requests.post('http://httpbin.org/post', files=files)
# print(response.text)

# demo12 -- 获取cookie
# response = requests.get('http://www.baidu.com')
# print(response.cookies)
# for key, value in response.cookies.items():
#     print(key + '=' + value)

# demo13 -- 会话维持 -- 1
# requests.get('http://httpbin.org/cookies/set/number/1234567890')
# response = requests.get('http://httpbin.org/cookies')
# print(response.text)

# demo13 -- 会话维持 -- 2
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/11223345566778')
# response = s.get('http://httpbin.org/cookies')
# print(response.text)

# demo14 -- 证书验证 --1
# response = requests.get('https://www.12306.cn')
# print(response.status_code)

# demo14 -- 证书验证 --2
# urllib3.disable_warnings()
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)

# demo14 -- 证书验证 --3
# response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
# print(response.status_code)

# demo15 -- 代理设置 -- 1
# proxies = {
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# }
# response = requests.get('https://www.taobao.com', proxies=proxies)
# print(response.status_code)

# demo15 -- 代理设置 -- 2
# proxies = {
#     'http': 'https://user:password@127.0.0.1:9743/'
# }
# response = requests.get('https://www.taobao.com', proxies=proxies)
# print(response.status_code)

# pip install 'requests[socks]'
# demo15 -- 代理设置 -- 3
# proxies = {
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# }
# response = requests.get('https://www.taobao.com', proxies=proxies)
# print(response.status_code)

# demo16 -- 超时设置 --1
# response = requests.get('https://www.taobao.com', timeout=0.1)
# print(response.status_code)

# demo16 -- 超时设置 --2
# try:
#     response = requests.get('http://httpbin.org/get', timeout=1)
#     print(response.status_code)
# except:
#     print('TimeOut')

# demo17 -- 认证设置 --1
# r = requests.get('http://120.27.34.24:9001', auth=HTTPBasicAuth('user', '123'))
# print(r.status_code)

# demo17 -- 认证设置 --2
# r = requests.get('http://120.27.34.24:9001', auth=('user', '123'))
# print(r.status_code)

# demo18 -- 异常处理 -- 1
try:
    response = requests.get('http://httpbin.org/get', timeout=0.1)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
except HTTPError:
    print('Http Error')
except RequestException:
    print('Error')

# demo18 -- 异常处理 -- 2
try:
    response = requests.get('http://httpbin.org/get', timeout=0.1)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
except ConnectionError:
    print('Connection Error')
except RequestException:
    print('Error')