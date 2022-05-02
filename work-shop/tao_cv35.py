#ตอนที่ 39 - รู้จักกับ Morphological

from operator import le
import cv2
import matplotlib.pyplot as plt

#import ภาพเข้ามาโดยเป็นเเบบ grayscale
img = cv2.imread("D:\Destop\Tao-OpenCV\python-opencv-main\image\CoinNoise.png",0)

thresh , result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)

titles = ["ORIGINAL","THRESH"]
images = [img,result]

#plot graph
for i in range(len(images)):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
