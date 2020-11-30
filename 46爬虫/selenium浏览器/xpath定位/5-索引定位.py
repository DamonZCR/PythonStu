from selenium import webdriver
import time
'''同意标签下同类型标签索引操作。
1.如果一个元素它的兄弟元素跟它的标签一样，这时候无法通过层级定位到。因为都是一个父亲生的，多胞胎兄弟。
2.虽然双胞胎兄弟很难识别，但是出生是有先后的，于是可以通过它在家里的排行老几定位到。
3.如下图三胞胎兄弟输入框。
4.用xpath定位老大、老二和老三（这里索引是从1开始算起的，跟Python的索引不一样）
'''
driver = webdriver.Chrome('..//chromedriver.exe')
driver.get('https://www.baidu.com')

# 依次点击百度首页左上方的新闻、hao123、地图三个选项。
# 使用两次属性定位。
driver.find_element_by_xpath("//div[@id='head']/div[@id='s-top-left']/a[1]").click()
# hao123
driver.find_element_by_xpath("//div[@id='head']/div[@id='s-top-left']/a[2]").click()
# 地图
driver.find_element_by_xpath("//div[@id='head']/div[@id='s-top-left']/a[3]").click()

# 使用纯索引定位。根据层级序号从 1 开始。
# 视频
driver.find_element_by_xpath("//div[@id='wrapper']/div[1]/div[3]/a[4]").click()

time.sleep(10)
driver.quit()