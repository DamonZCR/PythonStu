from selenium import webdriver
import time
import requests
'''此程序需要在弹出的微博界面自己登录微博，并搜索'全部艺人活跃粉丝榜‘
在这个搜索内容下爬取关于'全部艺人活跃粉丝榜的图片，但是程序实现只能简单获得。'''

url = 'https://weibo.com/'
driver = webdriver.Chrome('../geckodriver.exe')
driver.get(url)

time.sleep(100)
pic_urls = []
for page in range(2):
    # 抓取3个页面的信息
    for xiala in range(3):
        # 执行3次页面下拉（为什么要执行页面下拉？因为页面经过下拉之后会显示更多的信息）
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)  # 每次下拉之后暂停两秒（即给模拟的浏览器2秒的缓冲时间（加载出下拉页面））

    whole_mes = driver.find_elements_by_xpath('//div[@id = "pl_feedlist_index"]/div[1]')  # 一个页面的所有微博
    # 输出这页的列表的所有微博文字内容。
    print(whole_mes)
    for i in range(len(whole_mes)):
        # whole_mes[i].text 获取该区域的所有标签内的文字信息
        if '全部艺人活跃粉丝榜' in whole_mes[i].text:  # 选出符合条件的微博
            url = whole_mes[i].find_element_by_xpath(".//*[substring(@src,string-length(@src)-string-length("
                                  "'jpg')+1)='jpg']").get_attribute("src")
            # url = whole_mes[i].find_element_by_xpath('.//*[contains(@action-type,"fl_pics")]').get_attribute("src")
            url = url.replace('orj360', 'mw690')  # 经观察发现，url含orj360的图片较为模糊，换成mw690之后就是高清图了
            print(url)
            '''# 经观察发现，根据‘全部艺人活跃粉丝榜’这个条件筛选出来的微博中，有几条是我们不需要的（这几条是周榜和月榜的，而我们需要的是日榜），
            这几条的url都大于65，所以我们可以根据这一情况，把这几条微博过滤掉
            '''
            if len(url) == 65:
                pic_urls.append(url)
    print('++++++++++++++++++++++++++++++此页加载检索完毕++++++++++++++++++++++++++++++')
    driver.find_element_by_xpath("//a[contains(text(),'下一页')]").click()  # 执行 点击"下一页" 的操作
    time.sleep(2)  # 给模拟浏览器2秒的加载时间
    '''暂停15秒，因为爬虫的速度一般都比较快，所以操作会比较频繁。
    如果不暂停一下，很容易被新浪察觉出是爬虫在模拟人而不是人的实际操作。
    '''
    if page % 4 == 0:
        time.sleep(15)


headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'}
print("###################", len(pic_urls))
for i in range(len(pic_urls)):
    response = requests.get(pic_urls[i], headers=headers)
    with open('D:/Download/{}.jpg'.format(i), 'wb') as f: #将每张图片以jpg格式存入pic文件夹中
        f.write(response.content)
