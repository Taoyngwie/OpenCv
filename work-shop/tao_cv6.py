#ตอนที่ 8 - เปิดกล้องด้วย OpenCV

import cv2

cap = cv2.VideoCapture(0)

while(True):
   check ,frame = cap.read() #รับภาพจากกล้องโดยเป็นเเบบ เฟรม ต่อ เฟรม
    #ตัวเเปร check ไว้รับค่า boolean (ถ้าอ่านภาพได้จะเป็น true ถ้าไม่จะเป็น false)
    #ตัวเเปร frame คือภาพที่ได้จากการ cap จากการที่ตัวเเปร check เป็นจริง ถ้าเป็น false จะว่าง
   cv2.imshow("Output",frame) #เป็นการเเสดงภาพที่อ่านตอลดเวลา

   if cv2.waitKey(1) & 0xFF == ord("e"):#เมื่อกด e จะรอดีเล 1 วิ เเล้วปิดออกไป
       # 0xFF == ord("e") เเปลงจาก charecter to unicode เเล้วเปรียบเทียบกับ 0xFF
       break

cap.release() #ทำการคืนทรัพยากรให้เครื่อง
cv2.destroyAllWindows() #ทำการปิดหน้าต่าง