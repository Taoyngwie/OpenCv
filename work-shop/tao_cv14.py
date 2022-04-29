#ตอนที่ 15 - ใส่ข้อความในภาพ (Text)
import cv2
from cv2 import LINE_4
from cv2 import LINE_AA

#อ่านภาพ
img = cv2.imread("python-opencv-main\image\cat.jpg")

#กำหนดขนาด
imgresize = cv2.resize(img,(700,700))


#กำหนดข้อความบนภาพ
# putText(ภาพ,ข้อความ,พิกัดที่จะเเสดงข้อความ (x,y),font,ขนาดข้อความ,สี,ความหนา)
cv2.putText(imgresize,"CAT",(150,200),cv2.FONT_HERSHEY_COMPLEX,3.5,(0,0,255),cv2.LINE_AA)

cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()