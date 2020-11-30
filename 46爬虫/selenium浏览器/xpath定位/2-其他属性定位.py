from selenium import webdriver
import time
'''使用xpath其他属性定位：
'''

driver = webdriver.Chrome('..//chromedriver.exe')
driver.get('https://www.baidu.com')
time.sleep(3)

# 使用其他属性定位。
driver.find_element_by_xpath("//*[@autocomplete='off']").send_keys('py')
time.sleep(3)
driver.find_element_by_id('su').click()

time.sleep(10)

driver.quit()