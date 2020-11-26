from selenium import webdriver
import time
'''

'''
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')

time.sleep(5)
# 模糊匹配页面中的某个文本。
# 点击百度主页的hao123
driver.find_element_by_xpath("//*[contains(@id,'kw')]").send_keys('py')
driver.find_element_by_id('su').click()
time.sleep(5)
res = driver.find_element_by_xpath('.//png').get_attribute('scr')
print(res)
time.sleep(5)