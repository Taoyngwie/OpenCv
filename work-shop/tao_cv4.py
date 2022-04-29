#ตอนที่ 6 - กำหนดรูปแบบภาพ
import cv2

img = cv2.imread("D:\Destop\Tao-OpenCV\python-opencv-main\image\cat.jpg",0) #ใส่ 0 เพื่อให้ภาพเป็นภาพ gryscale
                                                                            #ใส่ -1 เพื่อ กำหนดโหมดของภาพพร้อมกับ alpha channal
#กำหนดขนาดใหม่ของภาพ
imgresize = cv2.resize(img,(400,400))

#เเสดงภาพ
cv2.imshow("output",imgresize) #คำสั่งเเสดงภาพ
cv2.waitKey(0) #กำหนดค่าดีเลย์ 0 วินาที
cv2.destroyAllWindows() #ปิดหน้าต่าง