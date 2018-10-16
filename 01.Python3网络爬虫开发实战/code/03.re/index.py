import re

# re.match -- 判断字符串从其实的位置开始匹配一个模式，如果不是起始位置配置成功的，直接返回none
# content = 'hello world 123456 aaa'
# result = re.match('^hello.*aaa', content)
# print(result)
# print(result.group())
# print(result.span())

# 贪婪匹配 -- result:6
# content = 'hello world 123456 aaa'
# result = re.match('^he.*(\d+).*aaa$', content)
# print(result)
# print(result.group(1))

# 非贪婪匹配 -- result:123456
# content = 'hello world 123456 aaa'
# result = re.match('^he.*?(\d+).*aaa$', content)
# print(result)
# print(result.group(1))

# 匹配模式 re.S :不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始，不会跨行
# content = '''Hello 123456 World_this
# is a Regex Demo
# '''
# result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
# print(result)

# 转义 -- $符号如果没有转义，是存在其他意思的，是无效的
# content = 'price is $5.00'
# result = re.match('price is $5.00', content)
# print(result)

# 转义 -- $符号如果没有转义，是存在其他意思的，是无效的
# content = 'price is $5.00'
# result = re.match('price is \$5\.00', content)
# print(result)

# re.search -- 扫描整个字符串并返回第一个成功的匹配 -- 为匹配方便，能用search就不用match
# 因为re.match是全匹配
# content = 'Extra string Hello 789789879 World 123 this World is a Demo'
# result = re.search('Hello.*?(\d+).*?World', content)
# print(result)
# print(result.group(1))

# re.findall -- 搜索字符串，以列表形式返回全部能匹配的子串
# content = '''hello 123
# aaa 456
#  bbb789
#  ccc\.963
# '''
# result = re.findall('\w.*?\s(\d+).*?', content)
# print(result)
# for item in result:
#     print(item)

# re.sub -- 替换字符串中每一个匹配的子串后返回替换后的字符串
# content = 'Hello 123456789 aaa'
# content = re.sub('\d+', 'Replacement', content)
# print(content)

# re.compile -- 讲正则字符串变异成正则表达式对象
# content = '''Hello 123456789 aaa
# is a Regex Demo'''
# pattern = re.compile('Hello.*Demo', re.S)
# result = re.match(pattern, content)
# print(content)
