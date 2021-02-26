import cv2
import numpy as np

start = cv2.getTickCount()

img = cv2.imread('iha.jpg')
res = np.uint8(np.clip((0.8 * img + 80), 0, 255))

end = cv2.getTickCount()

print((end - start) / cv2.getTickFrequency())