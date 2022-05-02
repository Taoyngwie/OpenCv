#ตอนที่ 52 - ตรวจจับขอบภาพด้วย Canny Method

import cv2

#รับภาพเข้ามาเเบบ grayscale
img = cv2.imread("D:\Destop\Tao-OpenCV\python-opencv-main\image\currency.jpg",0)

#กำหนดใช้งานเป็นแบบ แคนนี่
canny = cv2.Canny(img,50,200)

#แสดงผล
cv2.imshow("Original",img)
cv2.imshow("Canny",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()