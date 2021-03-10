from selenium import webdriver
import time
'''
未完成
'''
driver = webdriver.Chrome('../chromedriver.exe')
driver.get('https://www.baidu.com')

time.sleep(5)
# 模糊匹配页面中的某个文本。
# 点击百度主页的hao123
res = driver.find_element_by_xpath("//*[contains(@id,'kw')]")
print(res)
time.sleep(5)
driver.quit()
#res = driver.find_element_by_xpath('.//png').get_attribute('scr')
#print(res)
#time.sleep(5)




