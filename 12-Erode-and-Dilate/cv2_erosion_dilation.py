import cv2
import numpy as np


img = cv2.imread('j.bmp', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel)  
dilation = cv2.dilate(img, kernel)  

cv2.imshow('erosion/dilation', np.hstack((img, erosion, dilation)))
cv2.waitKey(0)



kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  
print(kernel)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  
print(kernel)

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5)) 
print(kernel)


kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) 


img = cv2.imread('j_noise_out.bmp', 0)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow('opening', np.hstack((img, opening)))
cv2.waitKey(0)


img = cv2.imread('j_noise_in.bmp', 0)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('closing', np.hstack((img, closing)))
cv2.waitKey(0)



img = cv2.imread('school.bmp', 0)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('morphological gradient', np.hstack((img, gradient)))
cv2.waitKey(0)



tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('top hat', np.hstack((img, tophat)))
cv2.waitKey(0)



blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('black hat', np.hstack((img, blackhat)))
cv2.waitKey(0)
