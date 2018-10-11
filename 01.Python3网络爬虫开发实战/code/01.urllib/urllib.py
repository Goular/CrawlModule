import urllib.request
import urllib.parse
import socket
import http.cookiejar

# demo1 -- 简单体验,获取网页的内容
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# demo2 -- POST(urlopen方法默认为GET，需要使用data变量后会自动变为POST请求)
# data = bytes(urllib.parse.urlencode({"word": "hello"}), encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

# demo3 -- 超时报错查询
# response = urllib.request.urlopen("http://httpbin.org/get", timeout=1)
# print(response.read())

# demo4 -- 超时报错处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.2)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('Time Out')

# demo5 -- 响应类型展示
# response = urllib.request.urlopen('https://www.python.org')
# print(type(response))

# demo6 -- 响应状态码，响应头
# response = urllib.request.urlopen('https://www.python.org')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server')) # Headers头部的特定字段

# demo7 -- 构造自定义的请求对象,替代url的方法的参数，同时能够构造更多的内容
# request = urllib.request.Request("https://python.org")
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# demo8 -- 构造头布局和请求body的POST 请求对象
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Germey'
# }
# data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
# req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

# demo9 -- 利用方法添加头部内容
# url = "http://httpbin.org/post"
# dict = {
#     'name': 'Germary'
# }
# data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
# req = urllib.request.Request(url=url, data=data, method='POST')
# req.add_header('User-Agent',
#                'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1')
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

# demo10 -- urllib的代理添加
# proxy_handler = urllib.request.ProxyHandler({
#     'http': 'http://110.40.13.5:80',
#     'https': 'https://127.0.0.1:9743'
# })
# opener = urllib.request.build_opener(proxy_handler)
# response = opener.open('http://httpbin.org/post')
# print(response.read().decode('utf-8'))

# demo11 -- 利用普通的http.cookiejar获取Cookie内容
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name + '=' + item.value)

# demo12 -- 利用普通的http.cookiejar.MozillaCookieJar保存Cookies到文件中
# filename = "cookies1.txt"
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# demo13 -- 利用普通的http.cookiejar.LWPCookieJar保存Cookies到文件中
# filename = 'cookie.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# demo14 -- 利用普通的http.cookiejar.LWPCookieJar读取Cookies
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookie.txt', ignore_expires=True, ignore_discard=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))
