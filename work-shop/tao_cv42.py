#ตอนที่ 50 - ตรวจจับขอบภาพด้วย Sobel Method

import cv2
import numpy as np
import matplotlib.pyplot as plt

#รับภาพเข้ามาเเบบ grayscale
img = cv2.imread("D:\Destop\Tao-OpenCV\python-opencv-main\image\currency.jpg",0)

#ปรับให้เป็นเเบบ sobel
    #หาเเบบเเนวนอน
sobelX = cv2.Sobel(img,-1,1,0)
    #หาเเบบเเนวตั้ง
sobelY = cv2.Sobel(img,-1,0,1)
#ผลจากการรวมขอบ x เเละ y
sobelXY = cv2.bitwise_or(sobelX,sobelY)


#นำมาแสดงผลโดยใช้งาน matpolotlib
images = [img,sobelX,sobelY,sobelXY]
titles = ["Original","SobelX","SobelY","SobelXY"]

for  i in range(len(images)):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],cmap="gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()


