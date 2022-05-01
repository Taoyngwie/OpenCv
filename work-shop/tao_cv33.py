#ตอนที่ 37 - การใช้งาน Adaptive Threshold
#Adaptive Threshold จะใช้งานเมื่อในภาพนั้นมีสีในระดับต่างกันมากๆในหลายๆจุดซึ่งทำให้วิธีเดิมไม่สามารถทำให้มองเห็นได้ชัดเจน

import cv2

#import ภาพเข้ามาโดยเป็นเเบบ grayscale
img = cv2.imread("D:\Destop\Tao-OpenCV\python-opencv-main\image\map.jpg",0)

#นำภาพมาเเปลงเป็นเเบบ Threshold Binary (Threshold เเบบปกติ)
thresh,th1 = cv2.threshold(img,128,255,cv2.THRESH_BINARY)

#นำภาพมาเเปลงเป็นเเบบ ADAPTIVE_THRESH_MEAN_C  (Adaptive Threshol)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,1)


#นำภาพมาเเปลงเป็นเเบบ ADAPTIVE_THRESH_GAUSSIAN  (Adaptive Threshol)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,1)


#แสดงผล output ออกมา
cv2.imshow("Threshold Original",th1)
cv2.imshow("ADAPTIVE_THRESH_MEAN_C",th2)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()

