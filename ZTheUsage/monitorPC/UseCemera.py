import cv2
import time
import os


def takephoto():
    cap = cv2.VideoCapture(0)
    f, frame = cap.read()
    os.chdir(r'D:/UnlockRecord/')
    # 获取时间
    dirtime = time.strftime("%m-%d", time.localtime())
    atime = dirtime.split('-')
    daydir = atime[0] + '月' + atime[1] + '日'
    if not os.path.isdir(r'./' + daydir):
        os.mkdir(r'./' + daydir)
    os.chdir(os.getcwd() + '/' + daydir)
    phadd = str(time.strftime("%H-%M-%S", time.localtime())) + '.jpg'
    # cv2.imwrite(phadd, frame*255)	
    cv2.imwrite(phadd, frame*5)
    cap.release()


if '__main__' == __name__:
    takephoto()
