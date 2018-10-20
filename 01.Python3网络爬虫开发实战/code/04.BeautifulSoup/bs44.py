from bs4 import BeautifulSoup

# demo01 -- 基本使用 -- 标签补全
# html = '''
# <html>
#     <head><title>Hello World</title></head>
#     <body>
#         <p>123545655555
#         <ul>
#             <li>8798798</li>
# '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# print(soup.title.string)

# demo02 -- 标签选择器
# html = '''
# <html>
#  <head>
#   <title>
#    Hello World
#   </title>
#  </head>
#  <body>
#   <p>
#    123545655555
#   </p>
#   <ul>
#    <li>
#     8798798
#    </li>
#   </ul>
#  </body>
# </html>
# '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.title)
# print(type(soup.title))
# print(soup.head)
# print(soup.p)

# demo3 -- 获取名称
# html = '''
# <html>
#  <head>
#   <title>
#    Hello World
#   </title>
#  </head>
#  <body>
#   <p>
#    123545655555
#   </p>
#   <ul>
#    <li>
#     8798798
#    </li>
#   </ul>
#  </body>
# </html>
# '''
# bs = BeautifulSoup(html, 'lxml')
# print(bs.title.name)

# demo4 -- 获取属性
# html = '''
# <html>
#  <head>
#   <title>
#    Hello World
#   </title>
#  </head>
#  <body>
#   <p class='abc cde' name='goular-88'>
#    123545655555
#   </p>
#   <ul>
#    <li name='goular'>
#     8798798
#    </li>
#   </ul>
#  </body>
# </html>
# '''
# bs = BeautifulSoup(html, 'lxml')
# print(bs.p.attrs['name'])
# print(bs.p['name'])

# demo5 -- 获取内容
# html = '''
# <html>
#  <head>
#   <title>
#    Hello World
#   </title>
#  </head>
#  <body>
#   <p class='abc cde' name='goular-88'>
#    123545655555
#   </p>
#   <ul>
#    <li name='goular'>
#     8798798
#    </li>
#   </ul>
#  </body>
# </html>
# '''
# bs = BeautifulSoup(html, 'lxml')
# print(bs.p.string)

# demo06 -- 嵌套选择
# html = '''
# <html>
#  <head>
#   <title>
#    Hello World
#   </title>
#  </head>
#  <body>
#   <p class='abc cde' name='goular-88'>
#    123545655555
#   </p>
#   <ul>
#    <li name='goular'>
#     8798798
#    </li>
#   </ul>
#  </body>
# </html>
# '''
#
# bs = BeautifulSoup(html, 'lxml')
# print(bs.head.title.string)

# demo07 -- 子节点
# html = '''
# <html>
#  <head>
#   <title>
#    Hello World
#   </title>
#  </head>
#  <body>
#   <p class='abc cde' name='goular-88'>
#    123545655555
#    <a href='http://www.baidu.com'><span>popopopeuuu</span></a>
#    abcdefhijklmnopq
#   </p>
#   <ul>
#    <li name='goular'>
#     8798798
#    </li>
#   </ul>
#  </body>
# </html>
# '''
# bs = BeautifulSoup(html, 'lxml')
# print(bs.p.contents)

# demo07 -- 子节点迭代器写法
# html = '''
# <html>
#  <head>
#   <title>
#    Hello World
#   </title>
#  </head>
#  <body>
#   <p class='abc cde' name='goular-88'>
#    123545655555
#    <a href='http://www.baidu.com'><span>popopopeuuu</span></a>
#    abcdefhijklmnopq
#   </p>
#   <ul>
#    <li name='goular'>
#     8798798
#    </li>
#   </ul>
#  </body>
# </html>
# '''
# bs = BeautifulSoup(html, 'lxml')
# # print(bs.p.children)
# for i, child in enumerate(bs.p.children):
#     print(i, child)

# # demo08 -- 子孙节点，打印所有的子孙情况
# html = '''
# <html>
#  <head>
#   <title>
#    Hello World
#   </title>
#  </head>
#  <body>
#   <p class='abc cde' name='goular-88'>
#    123545655555
#    <a href='http://www.baidu.com'><span>popopopeuuu</span></a>
#    abcdefhijklmnopq
#   </p>
#   <ul>
#    <li name='goular'>
#     8798798
#    </li>
#   </ul>
#  </body>
# </html>
# '''
# bs = BeautifulSoup(html, 'lxml')
# print(bs.p.descendants)
# for i, child in enumerate(bs.p.descendants):
#     print(i, child)
#
# # demo09 -- 父节点
# html = '''
# <html>
#  <head>
#   <title>
#    Hello World
#   </title>
#  </head>
#  <body>
#   <p class='abc cde' name='goular-88'>
#    123545655555
#    <a href='http://www.baidu.com'><span>popopopeuuu</span></a>
#    abcdefhijklmnopq
#   </p>
#   <ul>
#    <li name='goular'>
#     8798798
#    </li>
#   </ul>
#  </body>
# </html>
# '''
# bs = BeautifulSoup(html, 'lxml')
# print(bs.p.parent)


# demo09 -- 祖先节点
# html = '''
# <html>
#  <head>
#   <title>
#    Hello World
#   </title>
#  </head>
#  <body>
#   <p class='abc cde' name='goular-88'>
#    123545655555
#    <a href='http://www.baidu.com'><span>popopopeuuu</span></a>
#    abcdefhijklmnopq
#   </p>
#   <ul>
#    <li name='goular'>
#     8798798
#    </li>
#   </ul>
#  </body>
# </html>
# '''
# bs = BeautifulSoup(html, 'lxml')
# print(list(enumerate(bs.p.parents)))

# demo09 -- 兄弟节点
# html = '''
# <html>
#  <head>
#   <title>
#    Hello World
#   </title>
#  </head>
#  <body>
#   <p class='abc cde' name='goular-88'>
#    123545655555
#    <a href='http://www.baidu.com'><span>popopopeuuu</span></a>
#    <a href='http://www.baidu-2.com'><span>trytrytr</span></a>
#    abcdefhijklmnopq
#    <a href='http://www.baidu-3.com'><span>jhkjhkh</span></a>
#   </p>
#   <ul>
#    <li name='goular'>
#     8798798
#    </li>
#   </ul>
#  </body>
# </html>
# '''
# bs = BeautifulSoup(html, 'lxml')
# print(list(enumerate(bs.a.next_siblings)))  # 后面的兄弟节点
# print(list(enumerate(bs.a.previous_siblings)))  # 前面的兄弟节点

# demo10 -- 标准选择器 -- name
# html = '''
# <div class=panel>
#     <div class='panel-heading'>
#         <h4>Hello</h4>
#     </div>
#     <div class='panel-body'>
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# bs = BeautifulSoup(html, 'lxml')
# print(bs.find_all('ul'))
# print(type(bs.find_all('ul')[0]))

# demo10 -- 标准选择器 -- name
# html = '''
# <div class=panel>
#     <div class='panel-heading'>
#         <h4>Hello</h4>
#     </div>
#     <div class='panel-body'>
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# bs = BeautifulSoup(html, 'lxml')
# for ul in bs.find_all('ul'):
#     print(ul.find_all('li'))

# demo11 -- 标准选择器 -- attrs
# html = '''
# <div class=panel>
#     <div class='panel-heading'>
#         <h4>Hello</h4>
#     </div>
#     <div class='panel-body'>
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# bs = BeautifulSoup(html, 'lxml')
# print(bs.find_all(attrs={'id': 'list-1'}))
# print(bs.find_all(attrs={'class': 'panel-body'}))
# print(bs.find_all(class_='element')) # 特殊的属性可以通过查询文档获取
# print(bs.find_all(id='list-2')) # 特殊的属性可以通过查询文档获取

# # demo11 -- 标准选择器 -- text
# html = '''
# <div class=panel>
#     <div class='panel-heading'>
#         <h4>Hello</h4>
#     </div>
#     <div class='panel-body'>
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# bs = BeautifulSoup(html, 'lxml')
# print(bs.find_all(text='Bar'))

# demo11 -- 标准选择器 -- find
# html = '''
# <div class=panel>
#     <div class='panel-heading'>
#         <h4>Hello</h4>
#     </div>
#     <div class='panel-body'>
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# bs = BeautifulSoup(html, 'lxml')
# print(bs.find('ul'))
# print(type(bs.find('ul')))
# print(bs.find('page'))

# demo12 -- 标准选择器 -- css选择 --1
# html = '''
# <div class=panel>
#     <div class='panel-heading'>
#         <h4>Hello</h4>
#     </div>
#     <div class='panel-body'>
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# # select 与 find_all作用相似，都出列表
# bs = BeautifulSoup(html, 'lxml')
# print(bs.select('.panel .panel-body'))
# print(bs.select('ul li'))
# print(bs.select('#list-2 .element'))
# print(type(bs.select('ul')[0]))

# demo13 -- 标准选择器 -- css选择 --2
# html = '''
# <div class=panel>
#     <div class='panel-heading'>
#         <h4>Hello</h4>
#     </div>
#     <div class='panel-body'>
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# bs = BeautifulSoup(html, 'lxml')
# for ul in bs.select('ul'):
#     print(ul.select('li'))

# demo14 -- 标准选择器 -- css选择 -- attr
# html = '''
# <div class=panel>
#     <div class='panel-heading'>
#         <h4>Hello</h4>
#     </div>
#     <div class='panel-body'>
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# bs = BeautifulSoup(html, 'lxml')
# for ul in bs.select('ul'):
#     print(ul['id'])
#     print(ul.attrs['id'])

# demo15 -- 标准选择器 -- css选择 -- 获取内容
# html = '''
# <div class=panel>
#     <div class='panel-heading'>
#         <h4>Hello</h4>
#     </div>
#     <div class='panel-body'>
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# bs = BeautifulSoup(html, 'lxml')
# for li in bs.select('li'):
#     print(li.get_text())