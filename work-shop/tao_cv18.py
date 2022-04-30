#ตอนที่ 19 - แสดงภาพสีจากจุด Pixel

import cv2
import numpy
img = cv2.imread("D:\\Destop\\Tao-OpenCV\\python-opencv-main\\image\\spacetum.png")

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        imgcolor = numpy.zeros([300,300,3],numpy.uint8)
        #unint = unsigned integer เเละโดยที่ img color จะเเสดงผลออกมาเป็น array 3 d
        imgcolor[:] = [blue,green,red] #เอาจุดสีออกมาเป็นตัวเลขเพื่อใช้ในการเเสดง
        cv2.imshow("Result",imgcolor) #สร้างอีกหน้าต่าง
#เเสดงภาพ
cv2.imshow("Output",img) 
# ทำงานกับ mouse
cv2.setMouseCallback("Output",clickPosition) #เมื่อมีการทำงานร่วมกันกับเมาส์
cv2.waitKey(0) #จำนวนระยะเวลาในการแสดงภาพ
cv2.destroyAllWindows()

