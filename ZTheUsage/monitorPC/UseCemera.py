import cv2
import time
def takephoto():
    cap = cv2.VideoCapture(0)
    f, frame = cap.read()
    name = r'D:\\UnlockRecord\\' + str(time.strftime("%m-%d-%H-%M-%S",time.localtime())) + '.jpg'
    cv2.imwrite(name, frame)
    cap.release()


if '__main__' == __name__:
    takephoto()