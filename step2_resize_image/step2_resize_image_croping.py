import os
import cv2

img = cv2.imread(os.path.join('..', 'data', 'test_set', 'dogs', 'dog.4053.jpg'))

## crop the image
cropped_img = img[100:300, 150:400] ## [height, width]

cv2.imshow('original image', img)
cv2.imshow('cropped image', cropped_img)
cv2.waitKey(0)