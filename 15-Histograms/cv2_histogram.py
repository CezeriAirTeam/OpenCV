import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('hist.jpg', 0)


hist = cv2.calcHist([img], [0], None, [256], [0, 256])  


hist, bins = np.histogram(img.ravel(), 256, [0, 256])  


hist = np.bincount(img.ravel(), minlength=256)  



plt.hist(img.ravel(), 256, [0, 256])
plt.show()


plt.plot(hist)
plt.show()



equ = cv2.equalizeHist(img)
cv2.imshow('equalization', np.hstack((img, equ)))  
cv2.waitKey(0)


plt.hist(equ.ravel(), 256, [0, 256])
plt.show()



img = cv2.imread('tsukuba.jpg', 0)
equ = cv2.equalizeHist(img)  

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))  
cl1 = clahe.apply(img)

cv2.imshow('equalization', np.hstack((equ, equ, cl1)))  
cv2.waitKey(0)
