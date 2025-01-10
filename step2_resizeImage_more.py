import os
import cv2

img = cv2.imread(os.path.join('data', 'test_set', 'dogs', 'dog.4053.jpg'))


## cv2.risize(image, (width, height))
resized_img_not_right_ratio = cv2.resize(img, (243, 222)) ## this will not keep the ratio of height and width
resized_img_right_h_to_w_ratio = cv2.resize(img, (222,243)) ## this will keep the ratio of height and width
cv2.imshow('image', img)
cv2.imshow('resized image without correct h/w ratio', resized_img_not_right_ratio)
cv2.imshow('resized image with correct h/w ratio', resized_img_right_h_to_w_ratio)
cv2.waitKey(0)

cv2.destroyAllWindows()
print("original image shape is ", img.shape)
print("resized image without correct h/w ratio shape is ", resized_img_not_right_ratio.shape)
print("resized image with correct h/w ratio shape is ", resized_img_right_h_to_w_ratio.shape)