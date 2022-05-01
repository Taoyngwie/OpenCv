#ตอนที่ 35 - ปรับค่า Threshold ด้วย Trackbar

import cv2
import matplotlib.pyplot as plt

def display(value):
    pass


#หน้าต่างแสดงผล
cv2.namedWindow("Output")
cv2.createTrackbar("Value","Output",128,255,display)
                                    #128 = ค่าเริ่มต้น,255 = ค่าสูงสุด

while True:
    gray_img = cv2.imread("D:\\Destop\\Tao-OpenCV\\python-opencv-main\\image\\ant.jpg",0) #รับมาเป็นภาพสีเทา

    #ดึงค่าออกมาจาก เมธอด Trackbar
    thresh_value = cv2.getTrackbarPos("Value","Output") 

    #ปรับค่าในตอนเลื่อนตัวสไลด์ โดยที่รับค่ามาจากตัวแปรก่อนหน้า(thresh_value)
    thresh,result = cv2.threshold(gray_img,thresh_value,255,cv2.THRESH_BINARY) 

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
    cv2.imshow("Output",result) #นำค่า result ออกมาแสดงผล

cv2.destroyAllWindows()