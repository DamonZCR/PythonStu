'''程序问题：
再给照片命名时，不能使用变量作为名称的一部分，使用format也无法进行。
只要位置变量里带有变量就无法保存。'''
import cv2
import time
import os

def takephoto():
    cap = cv2.VideoCapture(0)
    f, frame = cap.read()
    os.chdir(r'D:/UnlockRecord/')
    # 获取时间
    newtime = time.strftime("%m-%d-%H-%M-%S",time.localtime())
    atime = newtime.split('-')
    daydir = atime[0] + '月' + atime[1] + '日'
    if not os.path.isdir(daydir):
        os.mkdir('./'+daydir)

    # phadd = atime[2] + '点' + atime[3] + '分' + atime[4] + '秒' + '.jpg'
    # phadd = "{0}/{1}点{2}分{3}秒.jpg".format(daydir, atime[2], atime[3], atime[4])
    phadd = str(time.strftime("%m-%d-%H-%M-%S", time.localtime())) + '.jpg'
    print(phadd)
    cv2.imwrite(phadd, frame)
    cap.release()


if '__main__' == __name__:
    takephoto()