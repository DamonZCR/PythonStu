from selenium import webdriver
import time
'''使用xpath属性定位：
三个等价的定位：("//标签名[ @属性= "属性值"]"）
以下定位的三个属性都是该标签的主要属性。
'''

# ./代表当前目录      ../代表父级目录       /根目录
driver = webdriver.Chrome('..//chromedriver.exe')
driver.get('https://www.baidu.com')

# 使用id 属性进行定位。
driver.find_element_by_xpath("//*[@id='kw']").send_keys('py')
time.sleep(3)
# 清空输入框，目前知道的唯一一种方法，通过查找后，使用clear()方法清空。
driver.find_element_by_id('kw').clear()
# 下面不进行清空，输入框就会出现 pythonpython3，不会覆盖的追加填写。
time.sleep(3)
driver.find_element_by_xpath("//*[@name='wd']").send_keys('python')
time.sleep(3)
driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys('python3')

driver.quit()