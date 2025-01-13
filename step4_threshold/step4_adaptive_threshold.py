import os
import cv2

img = cv2.imread(os.path.join('..', 'data', 'color', 'handwritten.jpg'))

## convert into gray image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## apply simple threshold
_, simple_thre = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

## apply adaptive threshold
## cv2.adaptiveThreshold(src, maxval, adaptiveMethod, thresholdType, blockSize, C)
## adaptiveMethod: mean, gaussian
## thresholdType: binary, binary inverse
## blockSize is the size of the neighborhood area to calculate the threshold value, 
   # it must be odd number because it is the size of the kernel to calculate the mean or weighted mean
## C: constant to subtract from mean or weighted mean
adaptive_thre = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 40)

cv2.imshow('Original', img)
cv2.imshow('Simple Threshold', simple_thre)
cv2.imshow('Adaptive Threshold', adaptive_thre)
cv2.waitKey(0)
cv2.destroyAllWindows()