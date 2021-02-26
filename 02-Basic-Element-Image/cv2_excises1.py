import cv2

img = cv2.imread('iha.jpg')
cv2.imshow('iha', img)

k = cv2.waitKey(0)

if k == ord('s'):
    cv2.imwrite('lena_save.bmp', img)
