import cv2

img = cv2.imread('iha.jpg')

px = img[100, 90]
print(px)  # [103 98 197]

px_blue = img[100, 90, 0]
print(px_blue)  # 103


img[100, 90] = [255, 255, 255]
print(img[100, 90])  # [255 255 255]


print(img.shape)  # (263, 247, 3)
height, width, channels = img.shape

print(img.size)  # 263*247*3=194883

print(img.dtype)  # uint8


face = img[100:200, 115:188]
cv2.imshow('face', face)
cv2.waitKey(0)


b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

b = img[:, :, 0]
cv2.imshow('b', b)
cv2.waitKey(0)
