import cv2
cap = cv2.VideoCapture(0)  # 注意：这个地方本文的图片里没有参数0，但是应该传入0
f, frame = cap.read()  # 此刻拍照
cv2.imwrite("example.png", frame)  # 将拍摄内容保存为png图片
cap.release()