#ตอนที่ 3 - การอ่านภาพ (Read Image)
import cv2

img = cv2.imread("D:\Destop\Tao-OpenCV\python-opencv-main\image\cat.jpg") #ดึงภาพเข้ามาในโปรเเกรม
print(img) #เเสดงเป็น numpy array  โดยที่เป็น array 3d
print(img.ndim) #เเสดงมิติของอาเรย์
print(type(img)) #เเสดงชนิด