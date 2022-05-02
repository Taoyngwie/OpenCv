#ตอนที่ 46 - ตัวกรองค่าเฉลี่ย (Mean Filter)
#ตอนที่ 48 - ตัวกรองเกาส์เซียน (Gaussian Filter)
import cv2
import numpy as np
import matplotlib.pyplot as plt

#original
img = cv2.imread("D:\\Destop\\Tao-OpenCV\\python-opencv-main\\image\\noise.png")

#filter
filter2d = cv2.filter2D(img,-1,np.ones((5,5),np.float32)/25)

#blur
mean = cv2.blur(img,(5,5))

#median
mblur=cv2.medianBlur(img,5)

#GaussianBlur
gblur = cv2.GaussianBlur(img,(5,5),1)
                                #ค่า sigma ยิ่งเยอะยิ่งใกล้เคียงค่าเบลอ

titles = ["ORIGINAL","FILTER2D","MEAN","MEDIAN BLUR","GAUSSIAN BLUR"]
images = [img,filter2d,mean,mblur,gblur]

for  i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
