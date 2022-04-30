#ตอนที่ 17 - แสดงพิกัดด้วย Mouse (Event)

import cv2
img = cv2.imread("D:\\Destop\\Tao-OpenCV\\python-opencv-main\\image\\tree.jpg")

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = str(x)+","+str(y) #เก็บเลขพิกัดแกน x เเละ y เอาไว้
        cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),cv2.LINE_4)
        cv2.imshow("Output",img)
#เเสดงภาพ
cv2.imshow("Output",img) 
# ทำงานกับ mouse
cv2.setMouseCallback("Output",clickPosition) #เมื่อมีการทำงานร่วมกันกับเมาส์
cv2.waitKey(0) #จำนวนระยะเวลาในการแสดงภาพ
cv2.destroyAllWindows()

