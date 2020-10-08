def findPerson(name = None):
    if name == None:
        name = input('请输入联系人姓名：')
    if name in contact:
        print(name+':'+contact.get(name))
        print(2*'\n')
    else:
        print('不存在此联系人！')
        choi = input('是否新建此联系人(YES/NO)：')
        if choi == 'YES':
            insertPerson(name)
        else:
            print(2*'\n')

def insertPerson(name = None):
    if name == None:
        name = input('请输入联系人姓名：')
    if name in contact:
        print('您输入的姓名再通讯录中已存在-->'+name+':'+contact.get(name))
        choi = input('是否修改此联系人(YES/NO)：')
        if choi == 'YES':
            num = input('请输入用户的联系电话：')
            contact[name] = str(num)
            print(2*'\n')
        else:
            print(2*'\n')
    else:
        num = input('请输入用户联系电话：')
        contact[name] = str(num)
        print(2*'\n')

def delPerson(name = None):
    if name == None:
        name = input('请输入联系人姓名：')
    if name in contact:
        contact.pop(name)
        print('删除成功！')
        print(2*'\n')
    else:
        print('不存在此联系人！')
        print(2*'\n')


print(" "+
"|---  欢迎进入通讯录程序--|\n "+
"|---  1：查询联系人资料 --|\n "+
"|---  2：插入新的联系人 --|\n "+
"|---  3：删除已有联系人 --|\n "+
"|---  4：退出通讯录程序 --|\n")


#声明一个字典
contact = dict()
ordnum = str()
while ordnum != '4':
    ordnum = input('请输入相关的指令代码：')
    if ordnum == '1':
        findPerson()
    elif ordnum == '2':
        insertPerson()
    elif ordnum == '3':
        delPerson()
print('感谢使用此程序！Made in 20200820')
        
    
