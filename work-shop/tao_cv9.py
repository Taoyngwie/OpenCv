#ตอนที่ 11 - การอัดวิดีโอ (Video Recorder)

from tabnanny import check
import cv2

cap = cv2.VideoCapture(0) #เปิดกล้อง
fourcc = cv2.VideoWriter_fourcc(*'XVID') #เขียน video

result = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480)) #ส่งออก video โดยกำหนด เฟรมเรท เเละ ขนาดการเเสดงผล

while(cap.isOpened()):
   check ,frame = cap.read() #รับภาพจากกล้องโดยเป็นเเบบ เฟรม ต่อ เฟรม
    #ตัวเเปร check ไว้รับค่า boolean (ถ้าอ่านภาพได้จะเป็น true ถ้าไม่จะเป็น false)
    #ตัวเเปร frame คือภาพที่ได้จากการ cap จากการที่ตัวเเปร check เป็นจริง ถ้าเป็น false จะว่าง
   gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #เเปลงเป็นภาพ grayscale
   if check == True: #ป้องกัน error ที่เกิดจาก video เล่นจบเเล้ว เเต่โปรเเกรมยังทำงานอยู่
          cv2.imshow("Output",frame) #เป็นการเเสดงภาพที่อ่านตอลดเวลา
          result.write(frame) #เป็นการเขียนจากที่เราบันทึกไว้ลงไป
          if cv2.waitKey(1) & 0xFF == ord("e"):#เมื่อกด e จะรอดีเล 1 วิ เเล้วปิดออกไป
              break
   else:
       break #ถ้าหมดเวลาเเล้วก็ให้ปิด video ไป


result.release()#ทำการคืนทรัพยากรให้เครื่อง
cap.release() #ทำการคืนทรัพยากรให้เครื่อง
cv2.destroyAllWindows() #ทำการปิดหน้าต่าง