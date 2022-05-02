#ตอนที่ 38 - เปรียบเทียบค่า BlockSize (เพื่อที่จะเลือกนำไปใช้งาน)

import cv2
import matplotlib.pyplot as plt
#import ภาพเข้ามาโดยเป็นเเบบ grayscale
img = cv2.imread("D:\Destop\Tao-OpenCV\python-opencv-main\image\map.jpg",0)

#กำหนดขนาด block
size = [3,5,9,17,33]

#นำมาแสดงผล(อันนี้เเสดงภาพแรก)
plt.subplot(231,xticks=[],yticks=[])
plt.imshow(img,cmap="gray")

#แสดงผลโดยที่จะเริ่มจากภาพที่ 2
for i in range(len(size)):
    #นำภาพมาเเปลงเป็นเเบบ ADAPTIVE_THRESH_MEAN_C  (Adaptive Threshol)
    result = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,size[i],1)
                                        #ADAPTIVE_THRESH_GAUSSIAN_C

    #ทำการพล็อตโดยใช้งาน forloop (โดยที่เราจะเริ่มจากภาพที่สอง เพราะภาพเเรก เราได้ทำการ plot ไปเเล้ว)
    plt.subplot(232+i) #เริ่มจากภาพที่ 2
    plt.title("%d"%size[i])
    plt.imshow(result,cmap="gray")
    plt.xticks([]),plt.yticks([])


plt.show()

