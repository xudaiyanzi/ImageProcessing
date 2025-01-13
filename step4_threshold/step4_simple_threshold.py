import os
import cv2

img = cv2.imread(os.path.join('..', 'data', 'color', 'bear.jpg'))

## convert into binary image

## step 1: convert into gray image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## step 2: apply threshold
## cv2.threshold(src, thresh, maxval, type), it returns 2 values: ret, thresholded image
## ret is the threshold value

## there are 6 types of thresholding: binary, binary inverse, trunc, to zero, to zero inverse, otsu

### binary: 
_, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

## apply with blur image to remove noise
k_size = 7
blur = cv2.blur(gray, (k_size, k_size))
_, blurred_binary = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)

cv2.imshow('Original', img)
cv2.imshow('Binary', binary)
cv2.imshow('Blurred Binary', blurred_binary)

cv2.waitKey(0)
cv2.destroyAllWindows()