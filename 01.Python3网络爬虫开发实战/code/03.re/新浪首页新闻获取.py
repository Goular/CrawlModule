import requests
import re

html = requests.get('https://www.sina.com.cn/').content
content = str(html, 'utf-8')
# re.S 用于忽略分行
pattern1 = re.compile('<ul\sclass="list-a\snews_top">(.*?)</ul>', re.S)
pattern2 = re.compile('<li.*?href="(.*?)".*?>(.*?)</a>.*?</li>', re.S)
result = re.findall(pattern1, content)
for item in result:
    print(item)
    news = re.findall(pattern2, item)
    for item2 in news:
        print(item2)