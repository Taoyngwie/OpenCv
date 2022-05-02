#ตอนที่ 45 - คอนโวลูชั่นภาพ ด้วย Filter2D
import cv2
from matplotlib import image
import numpy as np
import matplotlib.pyplot as plt

#original(ภาพนี้เป็น grayscale อยู่เเล้ว)
img = cv2.imread("D:\\Destop\\Tao-OpenCV\\python-opencv-main\\image\\noise.png")

#kernal


#convo
convo1 = cv2.filter2D(img,-1,np.ones((3,3),np.float32)/9)
convo2 = cv2.filter2D(img,-1,np.ones((5,5),np.float32)/25)

titles = ["ORIGINAL",'CONVOLUTION 3X3','CONVOLUTION 5X5']
images = [img,convo1,convo2]

for  i in range(len(images)):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
