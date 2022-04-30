#ตอนที่ 20 - สร้างเส้นเชื่อมโยง (Connect Point)

import cv2
import numpy
img = numpy.zeros([400,400,3]) #สร้างภาพตัวอย่างสำหรับนำมาสร้างจุดเชื่อมโยง

#img = cv2.imread("D:\\Destop\\Tao-OpenCV\\python-opencv-main\\image\\cat.jpg")

#ตัวเเปรสำหรับเก็บตำเเหน่งจุด 2 จุด
points = []

#วาดวงกลม 
# circle(ภาพ,ตำเเหน่งจุดศูนย์กลางวงกลม (x,y),รัศมี,สี,ความหนา)
def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,0,255),4) #ใช้สำหรับการสร้างจุดวงกลม
        points.append((x,y)) #ใช้ในการเก็บค่าตำเเหน่ง x,y เมื่อผู้ใช้ได้ทำการคลิกเมาส์
        print(points)
        if len(points)>=2: #เมื่อ points มากกว่าเท่ากับ 2 ให้เริ่มต้นสร้งจุดออกมา
            print(points)
            print("[-1] = ",points[-1]) #แสดงจากหลังมาหน้า
            print("[-2] = ",points[-2]) #แสดงจากหลังมาหน้า
            cv2.line(img,points[-2],points[-1],(0,255,0),5) #ลากเส้นจุด1เเละ2 เเบบต่อเนื่องกัน (จุดก่อนหน้ามาเชื่อมจุดล่าสุด)
        cv2.imshow("Output",img) #ใช้สำหรับการเเสดงผลจุดวงกลมออกมา

#เเสดงภาพ
cv2.imshow("Output",img) 
# ทำงานกับ mouse
cv2.setMouseCallback("Output",clickPosition) #เมื่อมีการทำงานร่วมกันกับเมาส์
cv2.waitKey(0) #จำนวนระยะเวลาในการแสดงภาพ
cv2.destroyAllWindows()

