import cv2
import os

img_original = cv2.imread(os.path.join('..', 'data', 'color', 'blurred_girl.png'))

k_size = 7

## Apply gaussian blur
img_g_blur = cv2.GaussianBlur(img_original, (k_size, k_size), 0)

## Apply median blur
img_m_blur = cv2.medianBlur(img_original, k_size)

## Apply bilateral filter
img_bilateral = cv2.bilateralFilter(img_original, k_size, 75, 75)

cv2.imshow('Original', img_original)
cv2.imshow('Gaussian Blur', img_g_blur) 
cv2.imshow('Median Blur', img_m_blur) ## Median filter is good for salt-and-pepper noise
cv2.imshow('Bilateral Filter', img_bilateral) ## Bilateral filter is good for preserving edges

cv2.waitKey(0)
cv2.destroyAllWindows()