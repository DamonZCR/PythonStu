#调用摄像头

import cv2
# 调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
capture = cv2.VideoCapture(0)
while True:
	# 从摄像头读取图片
	# 摄像头读取,ret为是否成功打开摄像头,true,false。 frame为视频的每一帧图像
	ret, frame = capture.read()

	# 反转摄像头的拍摄效果，1是镜面效果，0是上下翻转，-1是上下翻转的镜面，无此行是相反。
	frame = cv2.flip(frame, 1)
	# 给图像加上黑白色
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('Taking', gray)
	if cv2.waitKey(30) == ord('q'):
		# 关闭所有窗口，此行可省略
		cv2.destroyAllWindows()

		# 释放摄像头
		capture.release()
		break
