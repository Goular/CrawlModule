import requests
from requests.exceptions import RequestException
import re
from multiprocessing import Pool
import json

# 基础网址
baseUrl = 'http://maoyan.com/board/4?offset='
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
}
# 正则字符串
pattern = '<dd>.*?board-index.*?">(.*?)</i>.*?data-src="(.*?)".*?alt="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>.*?class="score".*?class="integer">(.*?)</i>.*?class="fraction">(.*?)</i>'


# 获取单个网页的内容
def get_one_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == requests.codes.ok:
            return response.text
        return None
    except RequestException:
        return None


# 获取正则处理后的内容
def parse_one_page(data):
    list = re.findall(pattern, data, re.S)
    for item in list:
        yield {
            'index': int(item[0]),
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': float(item[5] + item[6])
        }


# 将数据内容写到文件
def write_to_file(data):
    with open('result.txt', 'a', encoding='utf-8')as file:
        file.write(json.dumps(data, ensure_ascii=False) + '\n')
        file.close()


def main(offset):
    url = baseUrl + str(offset * 10)
    # 获取网页文本内容
    html = get_one_page(url)
    if html != None:
        # 进行正则分析内容
        for item in parse_one_page(html):
            write_to_file(item)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i for i in range(10)])
