#ตอนที่ 54 - ตรวจจับการเคลื่อนไหว (Motion Detection)
import cv2
from cv2 import blur 
cap = cv2.VideoCapture("D:\Destop\Tao-OpenCV\python-opencv-main\image\Walking.mp4")

#เเยกออกมาไว้หาเส้น contours ตอนที่มีการเคลื่อนไหว
check ,frame1 = cap.read()
check ,frame2 = cap.read()

while(cap.isOpened()):
   if check == True: #ป้องกัน error ที่เกิดจาก video เล่นจบเเล้ว เเต่โปรเเกรมยังทำงานอยู่

          #หาผลต่างของค่าที่มาจาก frame1 เเละ frame2 เพื่อหาค่าความคลาดเคลื่อนของเเต่ละเฟรม ใช้ในการหาวัตถุเคลื่อนที่
          motiondiff = cv2.absdiff(frame1,frame2)
          #นำภาพมาแปลงเป็น  grayscale 
          gray = cv2.cvtColor(motiondiff,cv2.COLOR_BGR2GRAY)

          #ใส่ความเบลอเข้าไปในวัตถุเพื่อพื้นที่จะได้มีความชัดเจนยิ่งขึ้น
          blur = cv2.GaussianBlur(gray,(5,5),0)

          #ใส่ threshold เพื่อเเยกรายละเอียดภายในภาพ
          thresh,result = cv2.threshold(blur,15,255,cv2.THRESH_BINARY)

          #นำมาขยายพื้นที่ต่อโดยใช้งาน dilation
          dilation = cv2.dilate(result,None,iterations=3)
        
          #นำภาพจากทีได้มาหาเส้น Contours
          contours,hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
            #-> ได้ผลลัพธ์เป็นเส้น contour กับ ลำดับชั้น

            #นำเส้น contours มาทำเป็นภาพสี 
          cv2.drawContours(frame1,contours,-1,(0,255,0),2)
                            #ใช้งาน frame1 เพราะว่าเรามาร์คเส้นcontoursไว้ที่เฟรม1

        #แสดงผลภาพ
          cv2.imshow("Output",frame1) #เป็นการเเสดงภาพที่อ่านตอลดเวลา


          #สร้างการขยับจาก frame1 ไปที่ frame2 
          frame1 = frame2
          check,frame2 = cap.read()
        
          if cv2.waitKey(1) & 0xFF == ord("e"):#เมื่อกด e จะรอดีเล 1 วิ เเล้วปิดออกไป
              break
   else:
       break #ถ้าหมดเวลาเเล้วก็ให้ปิด video ไป


cap.release() #ทำการคืนทรัพยากรให้เครื่อง
cv2.destroyAllWindows() #ทำการปิดหน้าต่าง