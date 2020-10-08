import easygui as g

alist = ['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
msgstr = '【*真实姓名】为必填项,\n【*手机号码】为必填项，\n【*E-mail】为必填项'
infomsg = list()

infomsg = g.multenterbox(msgstr,'账号中心',fields=alist)
while 1:
    if '' in (infomsg[0],infomsg[1],infomsg[3],infomsg[5]):
        infomsg = g.multenterbox('请填写完整所有选项', '账号中心', fields=alist,values=infomsg)
    else:      #还可以添加其他判断条件
        break
print(infomsg)
