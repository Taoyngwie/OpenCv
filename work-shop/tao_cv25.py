# ตอนที่ 26 - ตรวจจับดวงตาและใบหน้าจากภาพ

import cv2

#อ่านภาพ
img = cv2.imread("D:\Destop\Tao-OpenCV\python-opencv-main\image\girl.jpg") #ดึงภาพเข้ามาในโปรเเกรม

#ตรวจจับใบหน้า
face_cascade = cv2.CascadeClassifier("D:\\Destop\\Tao-OpenCV\\python-opencv-main\\Detect\\haarcascade_frontalface_default.xml")
#ตรวจจับดวงตา
eye_cascade = cv2.CascadeClassifier("D:\\Destop\\Tao-OpenCV\\python-opencv-main\\Detect\\haarcascade_eye_tree_eyeglasses.xml")

#เเปลงจากภาพสีเป็น grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#ตรวจจับใบหน้า
scaleFactor = 1.2 #กำหนดให้ย่อขนาดลงเป็นสัดส่วน (ค่าเริ่มต้น ลดลง 10 %) 
minNeighber = 5 #มันคือค่า thresholding คือค่าที่ใช้ในการตรวจสอบ grayscale ที่ใกล้ที่สุด (ค่าเริ่มต้น) 
                            #พูดง่ายๆก็คือส่วนที่ใกล้เคียงกันกับใบหน้ามากที่สดนั่นเอง
face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)
                            #detectMultiScale = เมธอดที่ใช้ในการตรวจจับใบหน้า

#ตรวจจับดวงตา
eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)
                        #detectMultiScale = เมธอดที่ใช้ในการตรวจจับดวงตา
      
#สร้างกล่องสี่เหลี่ยม (โดยที่จะตรวจจับพร้อมกัน หน้า + ดวงตา)
for (x,y,w,h) in face_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=5)
    for(ex,ey,ew,eh) in eye_detect:
      cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255,0,0),thickness=5)

#เเสดงภาพ
cv2.imshow("output",img) #คำสั่งเเสดงภาพ
cv2.waitKey(delay=5000) #กำหนดค่าดีเลย์ 5 วินาที
cv2.destroyAllWindows() #ปิดหน้าต่าง