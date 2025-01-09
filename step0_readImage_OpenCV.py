import cv2
import os

image_path = os.path.join('.', 'data', 'test_set','cats','cat.4001.jpg')

img = cv2.imread(image_path)

cv2.imshow('image', img)
cv2.waitKey(0)

## write image
cv2.imwrite(os.path.join('.', 'data', 'output', 'cat.4001_copy.jpg'), img)