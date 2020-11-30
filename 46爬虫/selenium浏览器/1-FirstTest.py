from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
'''***此程序实现selenium的基本使用，主要是滚动条的操作，滚动至底部和顶部的两种方法。***
添加浏览器的驱动火狐浏览器为geckodriver.exr 谷歌浏览器为chromedriver.exe
驱动放在python.exe同一目录下。'''

# 使用相对路径，如将此驱动直接放置python.exe下，不需要加位置参数。其中 ./代表当前目录
browser = webdriver.Chrome('./chromedriver.exe')
# 窗口最大化
browser.maximize_window()
browser.get('http://www.baidu.com')
# 断言，确定打开的网页就是目标网页的标题。
assert '百度一下，你就知道' in browser.title

# 找到网页中标签名为wd的输入框，输入IDEA
elem = browser.find_element_by_name('wd')
elem.send_keys('IDEA' + Keys.RETURN)
# browser.find_element('id', 'su').click()也是一种查找按钮ID，并点击的方法。

# 是程序停止5秒钟，等待网页加载完毕。如果网页不能加载完毕，滚动不会进行
time.sleep(3)
'''两种方法的滚动，第一种是window.scrollTo(0,document.body.scrollHeight)标识滚动到底部，而
window.scrollTo(0,0)是顶部。第二种就是使用像素的关系滚动。
'''
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# 第二种滚动到底部
# js = 'var action = document.documentElement.scrollTop=10000'
# browser.execute_script(js)
# 弹出alert提示框
browser.execute_script('alert("To Bottom")')
time.sleep(3)
browser.switch_to.alert.accept()


# 滚动回顶部的两种方法
time.sleep(3)
# browser.execute_script('window.scrollTo(0,0)')
browser.execute_script('document.documentElement.scrollTop=0')

time.sleep(8)
browser.quit()