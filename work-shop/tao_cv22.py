#ตอนที่ 23 - ตรวจจับใบหน้าจากวิดีโอ (Face Detection)

from tabnanny import check
import cv2

cap = cv2.VideoCapture("D:\\Destop\\Tao-OpenCV\\work-shop\\news.mp4")

#อ่านไฟล์สำหรับ classification
face_cascade = cv2.CascadeClassifier("D:\\Destop\\Tao-OpenCV\\python-opencv-main\\Detect\\haarcascade_frontalface_default.xml")



while(cap.isOpened()):
   check ,frame = cap.read() #รับภาพจากกล้องโดยเป็นเเบบ เฟรม ต่อ เฟรม
    #ตัวเเปร check ไว้รับค่า boolean (ถ้าอ่านภาพได้จะเป็น true ถ้าไม่จะเป็น false)
    #ตัวเเปร frame คือภาพที่ได้จากการ cap จากการที่ตัวเเปร check เป็นจริง ถ้าเป็น false จะว่าง
   if check == True: #ป้องกัน error ที่เกิดจาก video เล่นจบเเล้ว เเต่โปรเเกรมยังทำงานอยู่
          gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #ทำให้ภาพสีเป็น grayscale
          cv2.imshow("Output",gray_img) #เป็นการเเสดงภาพที่อ่านตอลดเวลา

          #จำเเนกใบหน้า
          scaleFactor = 1.2 #กำหนดให้ย่อขนาดลงเป็นสัดส่วน (ค่าเริ่มต้น ลดลง 10 %) 
          minNeighber = 5 #มันคือค่า thresholding คือค่าที่ใช้ในการตรวจสอบ grayscale ที่ใกล้ที่สุด (ค่าเริ่มต้น) 
                            #พูดง่ายๆก็คือส่วนที่ใกล้เคียงกันกับใบหน้ามากที่สดนั่นเอง

          face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)
                            #detectMultiScale = เมธอดที่ใช้ในการตรวจจับใบหน้า
        
          #แสดงตำเเหน่งที่เจอใบหน้า
          for (x,y,w,h) in face_detect:
            cv2.rectangle(frame,(x,y),(x+h,y+h),(0,255,0),thickness=5) #สร้างกล่องสี่เหลี่ยมขึ้นมา
            cv2.imshow("Output",frame)

          if cv2.waitKey(1) & 0xFF == ord("e"):#เมื่อกด e จะรอดีเล 1 วิ เเล้วปิดออกไป
              break
   else:
       break #ถ้าหมดเวลาเเล้วก็ให้ปิด video ไป


cap.release() #ทำการคืนทรัพยากรให้เครื่อง
cv2.destroyAllWindows() #ทำการปิดหน้าต่าง