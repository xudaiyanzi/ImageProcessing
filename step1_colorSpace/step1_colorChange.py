import os
import cv2

img_original = cv2.imread(os.path.join('..', 'data', 'color', 'bird.jpg'))

## covert the color space from BGR to RGB
img_rgb = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)

img_grey = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY) # in cv2, the grey is represented as 0-255, calculated by 0.299*R + 0.587*G + 0.114*B

img_hsv = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV) # in cv2, the HSV is represented as H: 0-179, S: 0-255, V: 0-255

cv2.imshow('bird', img_original)
cv2.imshow('bird_rgb', img_rgb)
cv2.imshow('bird_grey', img_grey)
cv2.imshow('bird_hsv', img_hsv)
cv2.waitKey(0)