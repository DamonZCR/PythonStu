from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
b = webdriver.Chrome("D:\\PythonPro\\FStudy\\46爬虫\\selenium浏览器\\chromedriver.exe", options=chrome_options)
b.get('http://www.baidu.com')
b.quit()