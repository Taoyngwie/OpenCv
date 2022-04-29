#ตอนที่ 7 - การเขียนภาพ (Export)

import cv2

img = cv2.imread("D:\Destop\Tao-OpenCV\python-opencv-main\image\cat.jpg",0) #ดึงภาพเข้ามาในโปรเเกรม
#กำหนดขนาดใหม่ของภาพ
imgresize = cv2.resize(img,(400,400))

cv2.imwrite("output.jpg",imgresize) #Export ภาพออกไป

#เเสดงภาพ
cv2.imshow("output",imgresize) #คำสั่งเเสดงภาพ
cv2.waitKey(0) #กำหนดค่าดีเลย์ 0 วินาที
cv2.destroyAllWindows() #ปิดหน้าต่าง