import cv2
import numpy as np


def track_back(x):
    pass


img = cv2.imread('sudoku.jpg', 0)
cv2.namedWindow('window')


cv2.createTrackbar('maxVal', 'window', 100, 255, track_back)
cv2.createTrackbar('minVal', 'window', 200, 255, track_back)

while(True):
    
    max_val = cv2.getTrackbarPos('maxVal', 'window')
    min_val = cv2.getTrackbarPos('minVal', 'window')

    edges = cv2.Canny(img, min_val, max_val)
    cv2.imshow('window', edges)


    if cv2.waitKey(30) == 27:
        break
