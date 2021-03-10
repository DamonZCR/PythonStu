from selenium import webdriver
import time
'''
1.如果一个元素，它的属性不是很明显，无法直接定位到，这时候我们可以先找它老爸（父元素）
2.找到它老爸后，再找下个层级就能定位到了
3.如百度首页，要定位的是input这个标签，它的老爸的id=s_kw_wrap.
4.要是它老爸的属性也不是很明显，就找它爷爷id=form
5.于是就可以通过层级关系定位到
'''
driver = webdriver.Chrome('..//chromedriver.exe')
driver.get('https://www.baidu.com')

# 想找输入标签<Entry输入框,它的父标签是<span,它的爷爷标签是<form.

# 找它父亲标签,这里一直失败。下面找他爷爷标签可以使用
# driver.find_element_by_xpath("//span[@id='s_kw_wrap']/Entry输入框").send_keys('py')
time.sleep(3)
driver.find_element_by_id('kw').clear()

# 通过它爷爷标签查找。
time.sleep(3)
driver.find_element_by_xpath("//form[@name='f']/span/input").send_keys('量子')
time.sleep(3)

# 通过孩子找爷爷。找到form表单：/..找到它的父亲，再加上一个找到它的爷爷。
a = driver.find_element_by_xpath("//*[@id='su']/../..")
# 输出form
print(a.tag_name)
# 输出form的class属性值fm
print(a.get_attribute('class'))

time.sleep(3)
driver.quit()

