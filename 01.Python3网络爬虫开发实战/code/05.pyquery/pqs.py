from pyquery import PyQuery as pq

# demo01 -- 字符串初始化使用
# html = '''
# <div>
#     <ul>
#         <li class='item-0'>first item</li>
#         <li class='item-1'><a href='link2.html'>second item</a></li>
#         <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
#         <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
#         <li class='item-0'><a href='link5.html'>fifth item</a></li>
#     </ul>
# </div>
# '''
# doc = pq(html)
# print(doc('li'))

# demo02 -- URL初始化 -- 如果是一个url，会自动获取网址的内容，同时变为pyquery对象
# doc = pq(url='http://www.baidu.com')
# print(doc('head'))

# demo03 -- 文件初始化，从文件获取内容
# doc = pq(filename='demo.html')
# print(doc('li'))

# demo04 -- 基本CSS选择器
# html = '''
# <div id='container'>
#     <ul class='list'>
#         <li class='item-0'>first item</li>
#         <li class='item-1'><a href='link2.html'>second item</a></li>
#         <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
#         <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
#         <li class='item-0'><a href='link5.html'>fifth item</a></li>
#     </ul>
# </div>
# '''
# doc = pq(html)
# print(doc('#container .list li'))

# demo05 -- 子元素
# html = '''
# <div id='container'>
#     <ul class='list'>
#         <li class='item-0'>first item</li>
#         <li class='item-1'><a href='link2.html'>second item</a></li>
#         <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
#         <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
#         <li class='item-0'><a href='link5.html'>fifth item</a></li>
#     </ul>
# </div>
# '''
# doc = pq(html)
# items = doc('.list')
# print(type(items))
# print(items)
# lis = items.find('li')
# print(type(lis))
# print(lis)
# items = lis.children()
# print(type(items))
# print(items)


# demo06 -- 子元素 -- 获取class的列表
# html = '''
# <div id='container'>
#     <ul class='list'>
#         <li class='item-0'>first item</li>
#         <li class='item-1'><a href='link2.html'>second item</a></li>
#         <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
#         <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
#         <li class='item-0'><a href='link5.html'>fifth item</a></li>
#     </ul>
# </div>
# '''
# doc = pq(html)
# items = doc('.list')
# items2 = items.children('.active')
# print(items2)

# demo07 -- 父元素 -- 单个父元素
# html = '''
# <div id='container'>
#     <ul class='list'>
#         <li class='item-0'>first item</li>
#         <li class='item-1'><a href='link2.html'>second item</a></li>
#         <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
#         <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
#         <li class='item-0'><a href='link5.html'>fifth item</a></li>
#     </ul>
# </div>
# '''
# doc = pq(html)
# items = doc('.list')
# container = items.parent()
# print(type(container))
# print(container)

# demo08 -- 父元素 -- 多个父元素
# html = '''
# <div class='wrap'>
#     <div id='container'>
#         <ul class='list'>
#             <li class='item-0'>first item</li>
#             <li class='item-1'><a href='link2.html'>second item</a></li>
#             <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
#             <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
#             <li class='item-0'><a href='link5.html'>fifth item</a></li>
#         </ul>
#     </div>
# </div>
# '''
# doc = pq(html)
# items = doc('.list')
# parents = items.parents()
# print(type(parents))
# print(parents)

# demo09 -- 父元素 -- 多个父元素 -- 带class的查询
# html = '''
# <div class='wrap'>
#     <div id='container'>
#         <ul class='list'>
#             <li class='item-0'>first item</li>
#             <li class='item-1'><a href='link2.html'>second item</a></li>
#             <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
#             <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
#             <li class='item-0'><a href='link5.html'>fifth item</a></li>
#         </ul>
#     </div>
# </div>
# '''
# doc = pq(html)
# items = doc('.list')
# parents = items.parents('.wrap')
# print(type(parents))
# print(parents)

# demo10 -- 兄弟节点
# html = '''
# <div class='wrap'>
#     <div id='container'>
#         <ul class='list'>
#             <li class='item-0'>first item</li>
#             <li class='item-1'><a href='link2.html'>second item</a></li>
#             <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
#             <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
#             <li class='item-0'><a href='link5.html'>fifth item</a></li>
#         </ul>
#     </div>
# </div>
# '''
# doc = pq(html)
# li = doc('.list .item-0.active')
# print(li.siblings()) # 不带参数查询
# print(li.siblings('.active')) # 带参数的查询

# demo11 -- 单个元素 -- 1
# html = '''
# <div class='wrap'>
#     <div id='container'>
#         <ul class='list'>
#             <li class='item-0'>first item</li>
#             <li class='item-1'><a href='link2.html'>second item</a></li>
#             <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
#             <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
#             <li class='item-0'><a href='link5.html'>fifth item</a></li>
#         </ul>
#     </div>
# </div>
# '''
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)

# demo11 -- 单个元素 -- 2
# html = '''
# <div class='wrap'>
#     <div id='container'>
#         <ul class='list'>
#             <li class='item-0'>first item</li>
#             <li class='item-1'><a href='link2.html'>second item</a></li>
#             <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
#             <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
#             <li class='item-0'><a href='link5.html'>fifth item</a></li>
#         </ul>
#     </div>
# </div>
# '''
# doc = pq(html)
# li = doc('li').items()
# print(type(li))
# print(li)
# for item in li:
#     print(item)

# demo12 -- 获取属性
# html = '''
# <div class='wrap'>
#     <div id='container'>
#         <ul class='list'>
#             <li class='item-0'>first item</li>
#             <li class='item-1'><a href='link2.html'>second item</a></li>
#             <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
#             <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
#             <li class='item-0'><a href='link5.html'>fifth item</a></li>
#         </ul>
#     </div>
# </div>
# '''
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a)
# print(a.attr('href'))
# print(a.attr.href)


# demo13 -- 获取文本
# html = '''
# <div class='wrap'>
#     <div id='container'>
#         <ul class='list'>
#             <li class='item-0'>first item</li>
#             <li class='item-1'><a href='link2.html'>second item</a></li>
#             <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
#             <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
#             <li class='item-0'><a href='link5.html'>fifth item</a></li>
#         </ul>
#     </div>
# </div>
# '''
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a)
# print(a.text())

# demo14 -- 获取HTML
# html = '''
# <div class='wrap'>
#     <div id='container'>
#         <ul class='list'>
#             <li class='item-0'>first item</li>
#             <li class='item-1'><a href='link2.html'>second item</a></li>
#             <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
#             <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
#             <li class='item-0'><a href='link5.html'>fifth item</a></li>
#         </ul>
#     </div>
# </div>
# '''
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# print(li.html())


# demo13 -- DOM操作 -- addClass，removeClass
# html = '''
# <div class='wrap'>
#     <div id='container'>
#         <ul class='list'>
#             <li class='item-0'>first item</li>
#             <li class='item-1'><a href='link2.html'>second item</a></li>
#             <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
#             <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
#             <li class='item-0'><a href='link5.html'>fifth item</a></li>
#         </ul>
#     </div>
# </div>
# '''
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.remove_class('active')
# print(li)
# li.add_class('active cl1')
# print(li)

# demo13 -- DOM操作 -- attr，css
# html = '''
# <div class='wrap'>
#     <div id='container'>
#         <ul class='list'>
#             <li class='item-0'>first item</li>
#             <li class='item-1'><a href='link2.html'>second item</a></li>
#             <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
#             <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
#             <li class='item-0'><a href='link5.html'>fifth item</a></li>
#         </ul>
#     </div>
# </div>
# '''
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.attr('name', 'links2301')
# print(li)
# li.css('font-size', '16px')
# print(li)

# demo14 -- DOM操作 -- remove
# html = '''
# <div class='wrap'>
#     Hello,World.
#     <p>This is a paragraph.</p>
# </div>
# '''
# doc = pq(html)
# wrap = doc('.wrap')
# print(wrap.text())
# print(wrap)
# wrap.find('p').remove()
# print(wrap)

# demo15 -- DOM操作 -- 伪类选择器
html = '''
<div class='wrap'>
    <div id='container'>
        <ul class='list'>
            <li class='item-0'>first item</li>
            <li class='item-1'><a href='link2.html'>second item</a></li>
            <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
            <li class='item-1 active'><a href='link4.html'>fourth item</a></li>
            <li class='item-0'><a href='link5.html'>fifth item</a></li>
        </ul>
    </div>
</div>
'''
doc = pq(html)
# li = doc('li:first-child')
# print(li)
# print(li.text())
# li = doc('li:last-child')
# print(li)
# print(li.text())
# li = doc('li:nth-child(2)')
# print(li)
# print(li.text())
# li = doc('li:gt(2)')
# print(li)
# print(li.text())
# li = doc('li:nth-child(2n)')
# print(li)
# print(li.text())
li = doc('li:contains(second)')
print(li)
print(li.text())
