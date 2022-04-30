#ตอนที่ 27 - ตรวจจับดวงตาและใบหน้าจากวิดีโอ

from tabnanny import check
import cv2

cap = cv2.VideoCapture("D:\Destop\Tao-OpenCV\python-opencv-main\image\Mark.mp4")

#ตรวจจับใบหน้า
face_cascade = cv2.CascadeClassifier("D:\\Destop\\Tao-OpenCV\\python-opencv-main\\Detect\\haarcascade_frontalface_default.xml")
#ตรวจจับดวงตา
eye_cascade = cv2.CascadeClassifier("D:\\Destop\\Tao-OpenCV\\python-opencv-main\\Detect\\haarcascade_eye_tree_eyeglasses.xml")



while(cap.isOpened()):
   check ,frame = cap.read() #รับภาพจากกล้องโดยเป็นเเบบ เฟรม ต่อ เฟรม
    #ตัวเเปร check ไว้รับค่า boolean (ถ้าอ่านภาพได้จะเป็น true ถ้าไม่จะเป็น false)
    #ตัวเเปร frame คือภาพที่ได้จากการ cap จากการที่ตัวเเปร check เป็นจริง ถ้าเป็น false จะว่าง
   if check == True: #ป้องกัน error ที่เกิดจาก video เล่นจบเเล้ว เเต่โปรเเกรมยังทำงานอยู่
          gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #ทำให้ภาพสีเป็น grayscale
          #ในที่นี้เราจะใช้ grayscale ในการประมวลผลเเต่ใช้ frame ในการเเสดงผล
        
        #ตรวจจับใบหน้า
          scaleFactor = 1.2 #กำหนดให้ย่อขนาดลงเป็นสัดส่วน (ค่าเริ่มต้น ลดลง 10 %) 
          minNeighber = 5 #มันคือค่า thresholding คือค่าที่ใช้ในการตรวจสอบ grayscale ที่ใกล้ที่สุด (ค่าเริ่มต้น) 
                                        #พูดง่ายๆก็คือส่วนที่ใกล้เคียงกันกับใบหน้ามากที่สดนั่นเอง
          face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)
                                        #detectMultiScale = เมธอดที่ใช้ในการตรวจจับใบหน้า

        #ตรวจจับดวงตา
          eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)
                                #detectMultiScale = เมธอดที่ใช้ในการตรวจจับดวงตา


        #สร้างกล่องสี่เหลี่ยม (โดยที่จะตรวจจับพร้อมกัน หน้า + ดวงตา)
          for (x,y,w,h) in face_detect:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=5)
                for(ex,ey,ew,eh) in eye_detect:
                    cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(255,0,0),thickness=5)
          
          cv2.imshow("Output",frame) #เป็นการเเสดงภาพที่อ่านตอลดเวลา
          if cv2.waitKey(1) & 0xFF == ord("e"):#เมื่อกด e จะรอดีเล 1 วิ เเล้วปิดออกไป
              break
   else:
       break #ถ้าหมดเวลาเเล้วก็ให้ปิด video ไป


cap.release() #ทำการคืนทรัพยากรให้เครื่อง
cv2.destroyAllWindows() #ทำการปิดหน้าต่าง