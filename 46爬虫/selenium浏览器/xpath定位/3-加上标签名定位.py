from selenium import webdriver
import time
'''
1.有时候同一个属性，同名的比较多，这时候可以通过标签筛选下，定位更准一点
2.如果不想制定标签名称，可以用*号表示任意标签
3.如果想制定具体某个标签，就可以直接写标签名称
'''

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 使用标签名，再使用id 属性进行定位。
driver.find_element_by_xpath("//input[@id='kw']").send_keys('py')
time.sleep(3)
# 清空输入框，目前知道的唯一一种方法，通过查找后，使用clear()方法清空。
driver.find_element_by_id('kw').clear()

time.sleep(3)
driver.find_element_by_xpath("//input[@class='s_ipt']").send_keys('python3')
time.sleep(3)

driver.quit()