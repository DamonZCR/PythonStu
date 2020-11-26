from selenium import webdriver
import time
'''
模糊匹配，可以使用包含、以开始、已结束的模糊查找
'''
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')

time.sleep(5)
# 模糊匹配页面中的某个文本。
# 点击百度主页的hao123
driver.find_element_by_xpath("//*[contains(text(),'hao123')]").click()
time.sleep(5)

# 模糊匹配包含某个属性
# 在百度输入框输入py
driver.find_element_by_xpath("//*[contains(@id,'kw')]").send_keys('py')
time.sleep(5)

# 模糊匹配以什么未结束的属性值，第一行暂未支持，先只能使用第二行代替。
# 在百度输入框追加python
# driver.find_element_by_xpath("//*[ends-with(@id,'kw')]").send_keys('python')
driver.find_element_by_xpath("//input[substring(@id,string-length(@id)-string-length("
                             "'kw')+1)='kw']").send_keys('python')
time.sleep(5)

# 匹配以什么未开始的属性值
# 点击百度一下的按钮。
driver.find_element_by_xpath("//*[starts-with(@id,'su')]").click()
time.sleep(5)

# 无法使用，原因未知。
# driver.find_element_by_xpath("//*[matchs(text(),'hao13')]").click()

time.sleep(10)
driver.quit()