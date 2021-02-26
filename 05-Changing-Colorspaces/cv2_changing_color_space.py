import cv2
import numpy as np

img = cv2.imread('iha.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
cv2.imshow('gray', img_gray)
cv2.waitKey(0)


flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)


blue = np.uint8([[[255, 0, 0]]])
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
print(hsv_blue)  # [[[120 255 255]]]


capture = cv2.VideoCapture(0)

lower_blue = np.array([100, 110, 110])
upper_blue = np.array([130, 255, 255])

while(True):
    ret, frame = capture.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) == ord('q'):
        break
