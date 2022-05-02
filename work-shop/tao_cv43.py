#ตอนที่ 51 - ตรวจจับขอบภาพด้วย Laplacian Method

import cv2

#รับภาพเข้ามาเเบบ grayscale
img = cv2.imread("D:\Destop\Tao-OpenCV\python-opencv-main\image\currency.jpg",0)

#กำหนดใช้งานเป็นแบบ ลาปาเซี่ยน
lap = cv2.Laplacian(img,-1)

#แสดงผล
cv2.imshow("Original",img)
cv2.imshow("Laplacian",lap)

cv2.waitKey(0)
cv2.destroyAllWindows()