import cv2

img = cv2.imread('iha.jpg')

hat_r = img[25:120, 50:220, 2]
cv2.imshow('hat', hat_r)
cv2.waitKey(0)
