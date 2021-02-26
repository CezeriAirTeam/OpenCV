import cv2

img = cv2.imread('iha.jpg', 0)


cv2.imshow('iha', img)
cv2.waitKey(0)

cv2.namedWindow('iha2', cv2.WINDOW_NORMAL)
cv2.imshow('iha2', img)
cv2.waitKey(0)


cv2.imwrite('iha_gray.jpg', img)
