import cv2

start = cv2.getTickCount()

img = cv2.imread('iha.jpg')

end = cv2.getTickCount()

print((end - start) / cv2.getTickFrequency())
