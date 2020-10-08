'''加载非二进制文件将会报错'''
import pickle 

afile = open('D:/pickle文件.txt','rb')
aa = pickle.load(afile)
print(aa)
afile.close()
