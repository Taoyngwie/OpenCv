#ตอนที่ 32 - ฟังก์ชั่น Threshold ใน OpenCV

import cv2

gray_img = cv2.imread("D:\Destop\Tao-OpenCV\python-opencv-main\image\gradient.png")


#ทำภาพเป็นเเบบบนารี่โดยใช้งาน Threshold เเบบต่างๆ

#เเบบที่ 1
thresh,th1 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
    #โดยค่าจากตัวเเปร thresh คือค่ากลางที่เราระบุจากค่าจุดเเบ่ง 128
    #ค่าจากตัวเเปร result คือรับค่ามาจาก แปลง grayscale ไปเป็น binary

#เเบบที่ 2
thresh,th2 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY_INV)
    #โดยค่าจากตัวเเปร thresh คือค่ากลางที่เราระบุจากค่าจุดเเบ่ง 128
    #ค่าจากตัวเเปร result คือรับค่ามาจาก แปลง grayscale ไปเป็น BINARY_INV

#เเบบที่ 3
thresh,th3 = cv2.threshold(gray_img,128,255,cv2.THRESH_TRUNC)
    #โดยค่าจากตัวเเปร thresh คือค่ากลางที่เราระบุจากค่าจุดเเบ่ง 128
    #ค่าจากตัวเเปร result คือรับค่ามาจาก แปลง grayscale ไปเป็น THRESH_TRUNC

#เเบบที่ 4
thresh,th4 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO)
    #โดยค่าจากตัวเเปร thresh คือค่ากลางที่เราระบุจากค่าจุดเเบ่ง 128
    #ค่าจากตัวเเปร result คือรับค่ามาจาก แปลง grayscale ไปเป็น THRESH_TOZERO

#เเบบที่ 5
thresh,th5 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO_INV)
    #โดยค่าจากตัวเเปร thresh คือค่ากลางที่เราระบุจากค่าจุดเเบ่ง 128
    #ค่าจากตัวเเปร result คือรับค่ามาจาก แปลง grayscale ไปเป็น TOZERO_INV


#Output ค่าต่างๆ
cv2.imshow("Original",gray_img) #เเสดง output ภาพออกมา
cv2.imshow("Binary",th1) #เเสดง output ภาพออกมา
cv2.imshow("Binary_INV",th2) #เเสดง output ภาพออกมา
cv2.imshow("TRUNC",th3) #เเสดง output ภาพออกมา
cv2.imshow("Tozero",th4) #เเสดง output ภาพออกมา
cv2.imshow("Tozero_inv",th5) #เเสดง output ภาพออกมา

cv2.waitKey(0) #ใส่เพื่อเเสดงค้างไว้
cv2.destroyAllWindows()

