#ตอนที่ 18 - ตรวจจับค่าสีด้วย Mouse (Event)

import cv2
img = cv2.imread("D:\\Destop\\Tao-OpenCV\\python-opencv-main\\image\\color.jpg")

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        text = str(blue)+","+str(green)+","+str(red) #เก็บเลขพิกัดแกน blue , green  เเละ red เอาไว้
        cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),cv2.LINE_4)
        cv2.imshow("Output",img)
#เเสดงภาพ
cv2.imshow("Output",img) 
# ทำงานกับ mouse
cv2.setMouseCallback("Output",clickPosition) #เมื่อมีการทำงานร่วมกันกับเมาส์
cv2.waitKey(0) #จำนวนระยะเวลาในการแสดงภาพ
cv2.destroyAllWindows()

