'''输出指定文件夹下的所有.txt文件中，含有被查找字符
的信息，信息包括：所在关键字所在文件名称地址，行数，行中的位置'''

import os

def findfile(addr):
    #获取该路径下所有的文件及文件夹名称
    #建立新的列表，存储当前文件夹下的所有文件内容,注意这里的列表是局部变量
    inallfile = os.listdir(addr)
    for onefile in inallfile:
        newaddr = addr + onefile
        if os.path.isfile(newaddr):
            if onefile.endswith('.txt'):#以.txt结尾
                txtfile.append(newaddr)     
        else:
            findfile(newaddr+'\\')
    del inallfile

#查找文件中的关键字
def findword(addrlist, aword):
    for addr in addrlist:
        ftxt = open(addr, 'r',encoding = 'UTF-8')
        #文件中的行列表
        filelist = list(ftxt)
        #关键字的行中位置列表,做成二维列表，每一维是该行的字符位置
        localist = list()
        #标记行数
        i = 1
        for oneline in filelist:
            if aword in oneline:
                wordflag = list()
                #loca代表查找到的关键字的位置
                loca, flag = -1, 0
                wordflag.append(i)
                while flag != -1:
                    loca = oneline.find(aword,loca+1)
                    flag = loca
                    if loca != -1:
                        wordflag.append(loca+1)
                #将这一行记录的关键字信息列表加入该文件的列表中
                localist.append(wordflag)
            i +=1
        #如果这个文件中含有要查找的关键字
        if len(localist) != 0:
            wordetail[addr] = localist
        ftxt.close()


fileaddr = input('请输入查找地址:')
aword = input('请输入要查找的关键字：')

txtfile = list()#查找到的.txt文件路径
wordetail = dict()#关键词的详细信息，以地址为键行数和位置形成的列表为值

findfile(fileaddr+'\\')
confirm = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：'%aword)
if confirm == 'YES'or 'yes':
    findword(txtfile, aword)
    for eachfile in wordetail:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('在文件【%s】中找到关键字【%s】'%(eachfile, aword))
        for eachline in wordetail[eachfile]:
            print('关键字的位置出现在第 '+str(eachline[0])+' 行，第'+str(eachline[1:])+'个位置')
else:
    print('再见！')








        

        
