import cv2
import random

img = cv2.imread('tut-2.jpg', -1)

tag = img[100:400, 600:900]
img[300:600, 500:800] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


