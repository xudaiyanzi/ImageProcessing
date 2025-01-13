import os
import cv2

img_original = cv2.imread(os.path.join('..', 'data', 'color', 'girl.jpg'))

k_size = 7 # kernel size, the larger the more blur

## there are many types of blur, here we use GaussianBlur
## 0 is the standard deviation of the Gaussian kernel
img_g_blur = cv2.GaussianBlur(img_original, (k_size, k_size), 0)

## just blur the image, not guassian blur
img_blur = cv2.blur(img_original, (k_size, k_size))

## blur the image with median filter
img_median = cv2.medianBlur(img_original, k_size)

## blur the image with bilateral filter, it can keep the edge of the image
img_bilateral = cv2.bilateralFilter(img_original, 9, 75, 75)

cv2.imshow('Original', img_original)
cv2.imshow('Gaussian Blur', img_g_blur)
cv2.imshow('Blur', img_blur)
cv2.imshow('Median', img_median)
cv2.imshow('Bilateral', img_bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()