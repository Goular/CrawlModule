from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from selenium.webdriver import ActionChains

# demo01 -- 基本使用
# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()

# demo02 -- 声明浏览器对象
# browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# browser = webdriver.phantomjs()
# browser = webdriver.Safari()

# demo03 -- 访问网页
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# print(browser.page_source)
# browser.close()

# demo04 -- 查找元素 -- 单个元素
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# input_fourth = browser.find_element(By.ID, 'q')
# print(input_first)
# print(input_second)
# print(input_third)
# print(input_fourth)
# browser.close()

# demo05 -- 查找元素 -- 多个元素 -- 写法一
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# lis = browser.find_element_by_css_selector('.service-bd li')
# print(lis)
# browser.close()

# demo05 -- 查找元素 -- 多个元素 -- 写法二
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# lis = browser.find_element(By.CSS_SELECTOR, '.service-bd li')
# print(lis)
# browser.close()

# demo06 -- 元素交互操作 -- 对获取的元素调用交互方法
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input = browser.find_element_by_id('q')
# input.send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()

# demo07 -- 元素交互操作 -- 交互动作 -- 将动作附加到动作链串行执行
# browser = webdriver.Chrome()
# url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source,target)
# actions.perform()

# demo08 -- 执行Javascript
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

# demo09 -- 获取元素信息 -- 获取属性
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))
# browser.close()

# # demo10 -- 获取文本值
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)
# browser.close()

# demo11 -- 获取ID,位置，标签名，大小
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)
# browser.close()

# demo12 -- iFrame
# browser = webdriver.Chrome()
# url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# print(source)
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('No Logo')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)

# demo13 -- 等待 -- 隐式等待
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)

# demo14 -- 等待 -- 显示等待
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)

# demo15 -- 前进后退
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.get('https://www.taobao.com')
# browser.get('https://www.qq.com')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()

# demo16 -- cookies
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'sina', 'domain': 'www.zhihu.com', 'value': 'Germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

# demo17 -- 选项卡管理
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to.window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to.window(browser.window_handles[0])
# browser.get('https://www.qq.com')

# demo18 -- 异常处理 -- 1
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.find_element_by_id('hello')  # 这里会出现异常

# demo18 -- 异常处理
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()
