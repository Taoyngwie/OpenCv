#ตอนที่ 24 - ตรวจจับดวงตาจากภาพ (Eye Detection)

import cv2
from sklearn.preprocessing import scale

#อ่านภาพ
img = cv2.imread("D:\\Destop\\Tao-OpenCV\\python-opencv-main\\image\\girl.jpg")

#อ่านไฟล์สำหรับ classification
eye_Cascade = cv2.CascadeClassifier("D:\\Destop\\Tao-OpenCV\\python-opencv-main\\Detect\\haarcascade_eye_tree_eyeglasses.xml")

#ทำให้ภาพสีเป็น grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

#จำเเนกดวงตา
scaleFactor = 1.1 #กำหนดให้ย่อขนาดลงเป็นสัดส่วน (ค่าเริ่มต้น ลดลง 10 %) 
minNeighber = 3 #มันคือค่า thresholding คือค่าที่ใช้ในการตรวจสอบ grayscale ที่ใกล้ที่สุด (ค่าเริ่มต้น) 
                #พูดง่ายๆก็คือส่วนที่ใกล้เคียงกันกับใบหน้ามากที่สดนั่นเอง

eye_detect = eye_Cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)
                            #detectMultiScale = เมธอดที่ใช้ในการตรวจจับใบหน้า
#แสดงตำเเหน่งที่เจอใบหน้า
for (x,y,w,h) in eye_detect:
    cv2.rectangle(img,(x,y),(x+h,y+h),(0,255,0),thickness=5) #สร้างกล่องสี่เหลี่ยมขึ้นมา

#เเสดงภาพ
cv2.imshow("Output",img)
#cv2.imshow("Grayscale",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
