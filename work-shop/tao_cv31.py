#ตอนที่ 34 - เปรียบเทียบค่า Threshold Value

import cv2
import matplotlib.pyplot as plt


img = cv2.imread("D:\\Destop\\Tao-OpenCV\\python-opencv-main\\image\\ant.jpg")

#เเปลง BGR -> Grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#แสดงค่า Threshold  แบบต่างๆ
thresh_value = [50,100,130,200,230]

#แสดงการ plot
plt.subplot(231,xticks=[],yticks=[])
plt.title("Original")
plt.imshow(gray_img,cmap="gray")

#ใช้การวนลูปเพื่อนำภาพมาเเสดงผลในรูปเเบบของ Threshold  แบบต่างๆ ทีกำหนดไว้ภายในลิส 
for i in range(len(thresh_value)):
    thresh,result = cv2.threshold(gray_img,thresh_value[i],255,cv2.THRESH_BINARY)
    #โดยค่าจากตัวเเปร thresh คือค่ากลางที่เราระบุจากในลิสต์ thresh_value
    #ค่าจากตัวเเปร result คือรับค่ามาจาก แปลง grayscale ไปเป็น binary
    plt.subplot(232+i) #นำมาplotต่อจากอันที่เราพล็อตเเล้วก่อนหน้านี้
    plt.title("%d"%thresh_value[i])
    plt.imshow(result,cmap="gray") #แสดงภาพออกมา
    plt.xticks([]),plt.yticks([])

plt.show()


