import cv2
cap = cv2.VideoCapture(0)  # 注意：这个地方本文的图片里没有参数0，但是应该传入0
f, frame = cap.read()  # 此刻拍照

# 第三个参数，它针对特定的格式：对于JPEG，其表示的是图像的质量，用0 - 100的整数表示，默认95;对于png ,第三个参数表示的是压缩级别。默认为3.
# cv2.imwrite(file, img, format)
cv2.imwrite("example.png", frame)  # 将拍摄内容保存为png图片
cap.release()