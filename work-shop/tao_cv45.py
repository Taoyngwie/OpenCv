#ตอนที่ 53 - หาเส้นเค้าโครงภาพ (Contours)

import cv2

#รับภาพเข้ามาเเบบ grayscale
img = cv2.imread("D:\\Destop\\Tao-OpenCV\\python-opencv-main\\image\\ant.jpg")

#นำภาพมาแปลงเป็น  grayscale 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#ทำภาพ grayscale -> binary
thresh,result = cv2.threshold(gray,215,255,cv2.THRESH_BINARY)

#นำภาพจากทีได้มาหาเส้น Contours
contours,hierarchy = cv2.findContours(result,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#-> ได้ผลลัพธ์เป็นเส้น contour กับ ลำดับชั้น

#นำเส้น contours มาทำเป็นภาพสี 
cv2.drawContours(img,contours,-1,(0,255,0),2)


#Output
cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
