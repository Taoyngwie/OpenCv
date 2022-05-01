#ตอนที่ 30 - แสดงภาพด้วย Matplotlib

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:\Destop\Tao-OpenCV\python-opencv-main\image\girl.jpg")

#ว่าด้วยการเเสดงผล OpenCV -> rgb เเต่ matplotlib -> bgr(ทำให้สีออกมาเพี้ยนได้)
#ดังนั้นเพื่อไม่ให้สีในฝั่งของ matplotlib เพี้ยนจึงต้อง มีการสลับ chanall สี จาก bgr -> rgb

#เเสดงรูปภาพจากในฝั่งของ openCV
cv2.imshow("Output",img)

#ทำการเเปลงสี จาก bgr -> rgb เพื่อให้ฝั่งของ matplotlib สีไม่เพี้ยน
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#เเสดงรูปภาพในฝั่งของ matplotlib
plt.imshow(img)
plt.show()