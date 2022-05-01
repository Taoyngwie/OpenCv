#ตอนที่ 28 - การสร้าง Color Trackbar

import cv2
import numpy as np #ใช้ในการสร้างภาพสีดำ

#ใช้ตัว numpy ในการสร้างรูปภาพสีดำขึ้นมา
img = np.zeros((200,250,3),np.uint8)

#กำหนดสร้างหน้าต่าง windown
cv2.namedWindow("Color Trackbar")

#เมธอดไว้ใช้งานร่วมกันกัน Tracker
def display(value):
  print(value)

#เริ่มต้นสร้าง Tracker
cv2.createTrackbar("B","Color Trackbar",0,255,display)
cv2.createTrackbar("G","Color Trackbar",0,255,display)
cv2.createTrackbar("R","Color Trackbar",0,255,display)

#เเสดงผลการทำงาน
while True:
  cv2.imshow("Color Trackbar",img)#output

  if cv2.waitKey(1) & 0xFF == ord("e"):
    break

  #ดึงค่าจาก Trackbar
  blue = cv2.getTrackbarPos("B","Color Trackbar")
  green = cv2.getTrackbarPos("G","Color Trackbar")
  red = cv2.getTrackbarPos("R","Color Trackbar")

  #กำหนดค่าใส่ลงไปเพื่อที่จำนำไปใช้งาน
  img[:] = [blue,green,red]


cv2.destroyAllWindows()
