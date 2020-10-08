'''快捷键：shirft + enter 可以在python中执行该行'''
import pickle

afile = open('D:/pickle文件.txt','wb')
ss = [2,2,3,4,('这是一个数据信息',1),['数据信息']]
pickle.dump(ss,afile)
afile.close()