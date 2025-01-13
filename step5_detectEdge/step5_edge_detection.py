import cv2
import os
import numpy as np

img = cv2.imread(os.path.join('..', 'data', 'color', 'basketball.jpg'))

## apply edge detection
## cv2.Canny(image, minVal, maxVal), minVal and maxVal are the minimum and maximum intensity gradient values
edges = cv2.Canny(img, 100, 200) # play around with the values to get the good result

## try with dilate and erode: 
## kernel is a matrix which is used to convolve the image,
## cv2.dilate(image, kernel, iterations): which is used to increase the area of the white region in the image
## cv2.erode(image, kernel, iterations): which is used to decrease the area of the white region in the image
## iterations is the number of times the operation is applied

k_size = 2
kernel = np.ones((k_size, k_size), np.uint8)
dilated = cv2.dilate(edges, kernel)

## apply erode after dilate because dilate will increase the area of the white region
## by applying erosion after dilation, we can remove the noise
eroded = cv2.erode(dilated, kernel) 

cv2.imshow('Original Image', img)
cv2.imshow('Edge Detection', edges)
cv2.imshow('Dilated Image', dilated)
cv2.imshow('Eroded Image', eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()