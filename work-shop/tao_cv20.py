#ตอนที่ 21 - ตรวจจับกลุ่มวัตถุจากสี (Detect Object)

import re
import cv2
import numpy #เอาไว้ใช้ในการเทียบช่วงของสี

while True :
    img = cv2.imread("D:\\Destop\\Tao-OpenCV\\python-opencv-main\\image\\ball2d.jpg")
    img = cv2.resize(img,(400,400))


    #ช่วงของสีที่เราต้องการใช้หา
    lower = numpy.array([5,111,10]) #ช่วงของสีเขียวที่เข็มที่สุด สามารถไปกดเปิดดูได้จากใน photoshop 
    upper = numpy.array([124,255,133]) #ช่วงของสีเขียวที่บางที่สุด สามารถไปกดเปิดดูได้จากใน photoshop 

    mask = cv2.inRange(img,lower,upper) #กดหนดช่วงของสีที่เรากำหนดจากภาพ

    #เอาภาพสี ไปใส่ในจุดสีขาว (โดยจากภาพที่เราสร้างมาจากในข้างต้น)
    result = cv2.bitwise_and(img,img,mask=mask) #เอา 2 ภาพมารวมกันเเล้วทำเป็นภาพใหม่

    if cv2.waitKey(0) & 0xFF == ord("e"): #คำสั่งที่ใช้ในการปิด
        break
    
    cv2.imshow("Original",img) #Output เเสดงภาพ
    cv2.imshow("Mask",mask) #output เเสดงค่าของชวงสี
    cv2.imshow("Result",result) #เเสดงภาพที่เราเติมสี

cv2.destroyAllWindows()


