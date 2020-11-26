from selenium import webdriver
import time
'''
1.如果一个元素，它的属性不是很明显，无法直接定位到，这时候我们可以先找它老爸（父元素）
2.找到它老爸后，再找下个层级就能定位到了
3.如百度首页，要定位的是input这个标签，它的老爸的id=s_kw_wrap.
4.要是它老爸的属性也不是很明显，就找它爷爷id=form
5.于是就可以通过层级关系定位到
'''
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 想找输入标签<input,它的父标签是<span,它的爷爷标签是<form.

# 找它父亲标签,这里一直失败。下面找他爷爷标签可以使用
# driver.find_element_by_xpath("//span[@id='s_kw_wrap']/input").send_keys('py')
time.sleep(3)
driver.find_element_by_id('kw').clear()

# 通过它爷爷标签查找。
time.sleep(3)
driver.find_element_by_xpath("//form[@name='f']/span/input").send_keys('python')
time.sleep(3)
driver.quit()

