#ตอนที่ 42 - Opening Morphological

import numpy as np
import cv2
import matplotlib.pyplot as plt

#import ภาพเข้ามาโดยเป็นเเบบ grayscale
img = cv2.imread("D:\Destop\Tao-OpenCV\python-opencv-main\image\CoinNoise.png",0)

thresh , result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)

#สร้าง อาเรย์เลข1
kernal = np.ones((2,2),np.uint8)

#ตัว เพื่อขยายพื้นที่ของภาพ
dilation = cv2.dilate(result,kernal,iterations=5) 
                        #ถ้าตัวทำซ้ำ(iterations)ยิ่งมีมากขอบขาวรอบๆก็จะมากขึ้น

#การกร่อนภาพ
erosion = cv2.erode(result,kernal,iterations=7)
                                #จำนวนรอบการทำซ้ำในการกลั่นภาพ
#opening
opennig = cv2.morphologyEx(result,cv2.MORPH_OPEN,kernal,iterations=5)
                                            #จำนวนรอบการทำซ้ำในภาพ

titles = ["ORIGINAL","THRESH","DILATION","EROSION","OPENING"]
images = [img,result,dilation,erosion,opennig]

#plot graph
for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
