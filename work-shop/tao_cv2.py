#ตอนที่ 4 - การแสดงผลภาพ (Display Image)
import cv2

img = cv2.imread("D:\Destop\Tao-OpenCV\python-opencv-main\image\cat.jpg") #ดึงภาพเข้ามาในโปรเเกรม

#เเสดงภาพ
cv2.imshow("output",img) #คำสั่งเเสดงภาพ
cv2.waitKey(delay=5000) #กำหนดค่าดีเลย์ 5 วินาที
cv2.destroyAllWindows() #ปิดหน้าต่าง