import cv2
import numpy as np

img = cv2.imread('drawing.jpg')

res = cv2.resize(img, (132, 150))

res2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

cv2.imshow('shrink', res), cv2.imshow('zoom', res2)
cv2.waitKey(0)


dst = cv2.flip(img, -1)
cv2.imshow('flip', np.hstack((img, dst)))  
cv2.waitKey(0)


rows, cols = img.shape[:2]

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('shift', dst)
cv2.waitKey(0)


M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -45, 0.5)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('rotation', dst)
cv2.waitKey(0)
