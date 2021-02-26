import cv2
import numpy as np

img = cv2.imread('lena.jpg')

blur = cv2.blur(img, (3, 3))



gau_blur = cv2.GaussianBlur(img, (3, 3), 0)


res = np.hstack((img, blur, gau_blur))
cv2.imshow('res', res)
cv2.waitKey(0)


img = cv2.imread('gaussian_noise.bmp')
blur = cv2.blur(img, (5, 5))  
gaussian = cv2.GaussianBlur(img, (5, 5), 1)  

res = np.hstack((img, blur, gaussian))
cv2.imshow('gaussian vs average', res)
cv2.waitKey(0)



img = cv2.imread('salt_noise.bmp', 0)

blur = cv2.blur(img, (5, 5))  
median = cv2.medianBlur(img, 5)  

res = np.hstack((img, blur, median))
cv2.imshow('median vs average', res)
cv2.waitKey(0)



img = cv2.imread('lena.jpg', 0)
gau = cv2.GaussianBlur(img, (5, 5), 0)  
blur = cv2.bilateralFilter(img, 5, 75, 75)  

res = np.hstack((img, gau, blur))
cv2.imshow('res', res)
cv2.waitKey(0)
