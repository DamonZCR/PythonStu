#新建用户
def newUser():
    name = input('请输入用户名：')
    while name in user:
        name = input('此用户名已经被使用，请重新输入：')
    user[name] = input('请输入密码：')
    print('注册成功，赶快去登录吧！')
    print(2*'\n')


#登录账号
def logIn():
    name = input('请输入用户名：')
    while name not in user:
        name = input('您输入的用户名不存在，请重新输入：')
    passw = input('请输入密码：')
    if passw == user[name]:
        print('欢迎进入本系统！')
    print(2*'\n')


#删除用户
def delUser():
    name = input('请输入用户名：')
    while name not in user:
        name = input('您输入的用户名不存在，请重新输入：')
    if name in user:
        user.pop(name)
        print('删除成功！')
        print(2*'\n')


#声明一个字典
user = dict()
ordnum = str()
while ordnum != 'Q' and ordnum != 'q':
    print(" "+
"|---  新建用户：N/n --|\n "+
"|---  登录账号：E/e --|\n "+
"|---  删除账号：D/d --|\n "+
"|---  退出程序：Q/q --|\n "+
"|---  请输入指令代码：",end='')
    ordnum = input()
    if ordnum == 'N' or ordnum == 'n':
        newUser()
    elif ordnum == 'E' or ordnum == 'e':
        logIn()
    elif ordnum == 'D' or ordnum == 'd':
        delUser()
        
print('感谢使用此程序！Made in 20200820')
        
    
