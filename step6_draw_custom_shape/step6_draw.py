import cv2
import os
import numpy as np

img = cv2.imread(os.path.join('..', 'data', 'color', 'whiteboard.png'))

print("original image shape: ", img.shape)

## add line
cv2.line(img, (100, 150), (250, 350), (255, 0, 0), 5) # (100, 150) is the starting point, (250, 350) is the ending point, (255, 0, 0) is the color, 5 is the thickness

## add rectangle
cv2.rectangle(img, (300, 200), (450, 400), (0, 255, 0), 3) # (300, 200) is the top-left corner, (450, 400) is the bottom-right corner, (0, 255, 0) is the color, 3 is the thickness

## add circle
cv2.circle(img, (500, 300), 50, (0, 0, 255), -1) # (500, 300) is the center, 50 is the radius, (0, 0, 255) is the color, -1 is the thickness, which means fill the circle

## add text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Hello World', (10, 500), font, 4, (0, 0, 0), 2, cv2.LINE_AA) # 'Hello World' is the text, (10, 500) is the bottom-left corner, font is the font style, 4 is the font scale, (0,0,0) is the color, 2 is the thickness, cv2.LINE_AA is the line type

cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()