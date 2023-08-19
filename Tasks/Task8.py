import cv2
pic1 = cv2.imread("D:\Pictures\l photos\IMG_20211013_171941-01-02.jpeg")
pic2 = cv2.imread("D:\Pictures\l photos\FB_IMG_1635598381581.jpg")
face = pic1[10:205, 45:205]
pic2[30:225, 40:200] = face
cv2.imshow("My Display", pic2)
cv2.waitKey(7000)
cv2.destroyAllWindows()