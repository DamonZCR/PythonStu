from selenium import webdriver
import time
'''
1.xpath还有一个比较强的功能，是可以多个属性逻辑运算的，可以支持与（and）、或（or）、非（not）
2.一般用的比较多的是and运算，同时满足两个属性
'''
driver = webdriver.Chrome('..//chromedriver.exe')
driver.get('https://www.baidu.com')

# 逻辑与
time.sleep(3)
driver.find_element_by_xpath("//*[@id='kw' and @name='wd']").send_keys('py')
time.sleep(5)
driver.quit()


