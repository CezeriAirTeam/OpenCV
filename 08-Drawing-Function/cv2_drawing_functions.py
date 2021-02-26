import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0, 0), (512, 512), (255, 0, 0), 5)



cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)



cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)



cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), -1)


pts = np.array([[10, 5],  [50, 10], [70, 20], [20, 30]], np.int32)

pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255))


line1 = np.array([[100, 20],  [300, 20]], np.int32).reshape((-1, 1, 2))
line2 = np.array([[100, 60],  [300, 60]], np.int32).reshape((-1, 1, 2))
line3 = np.array([[100, 100],  [300, 100]], np.int32).reshape((-1, 1, 2))
cv2.polylines(img, [line1, line2, line3], True, (0, 255, 255))



font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'ex2tron', (10, 500), font,
            4, (255, 255, 255), 2, lineType=cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
