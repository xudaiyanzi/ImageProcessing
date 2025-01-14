import os
import cv2

img = cv2.imread(os.path.join('..', 'data', 'color', 'shapes.jpg'))

## convert into binary inverted image because we want to find contours of white shapes with black background
## 1. convert into gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
## 2. apply thresholding
## cv2.threshold(src, thresh, maxval, type) 
ret, binary_inv = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

## find contours (countour means a curve joining all the continuous points along a boundary)
## cv2.findContours(image, mode, method)
## image: input image
## mode: contour retrieval mode. There are 4 modes: cv2.RETR_EXTERNAL, cv2.RETR_LIST, cv2.RETR_CCOMP, cv2.RETR_TREE
   ### cv.RETR_EXTERNAL: retrieves only the extreme outer contours
   ### cv.RETR_LIST: retrieves all of the contours without establishing any hierarchical relationships
   ### cv.RETR_CCOMP: retrieves all of the contours and organizes them into a two-level hierarchy. At the top level, there are external boundaries of the components. At the second level, there are boundaries of the holes
   ### cv.RETR_TREE: retrieves all of the contours and reconstructs a full hierarchy of nested contours
## method: contour approximation method. There are 3 methods: cv2.CHAIN_APPROX_NONE, cv2.CHAIN_APPROX_SIMPLE, cv2.CHAIN_APPROX_TC89_L1
    ### cv2.CHAIN_APPROX_NONE: stores absolutely all the contour points. That is, any 2 subsequent points (x1, y1) and (x2, y2) of the contour will be either horizontal, vertical or diagonal neighbors, that is, max(abs(x1-x2), abs(y2-y1))==1
    ### cv2.CHAIN_APPROX_SIMPLE: compresses horizontal, vertical, and diagonal segments and leaves only their end points. For example, an up-right rectangular contour is encoded with 4 points
    ### cv2.CHAIN_APPROX_TC89_L1: applies one of the flavors of the Teh-Chin chain approximation algorithm, which merges similar regions and reduces the number of points in a curve
    
## cv2.findContours() returns 2 values: contours, hierarchy
## contours: a list of contours
## hierarchy: optional output vector containing information about the image topology. It has as many elements as the number of contours. 
    # For each i-th contour contours[i], the elements hierarchy[i][0], hierarchy[i][1], hierarchy[i][2], 
    # and hierarchy[i][3] are set to 1, 2, 3, and 4, respectively.
contours, hierarchy = cv2.findContours(binary_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

## print contours which is larger than 1000
for contour in contours:
    if cv2.contourArea(contour) > 1000:
        # print('contour area:', cv2.contourArea(contour))
        # # draw the contour
        # # cv2.drawContours(image, contours, contourIdx, color, thickness)
        # cv2.drawContours(img, [contour], -1, (0, 255, 0), 3)
        
        ## find bounding box of contour
        x0, y0, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x0, y0), (x0+w, y0+h), (0, 255, 0), 2)

## draw contours
## cv2.drawContours(image, contours, contourIdx, color, thickness)
## image: input image
## contours: contours to draw
## contourIdx: index of contours to draw
## color: color of contours
## thickness: thickness of contours
# img_contour = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow('original_img', img)
cv2.imshow('gray', gray)
cv2.imshow('binary_inv', binary_inv)
# cv2.imshow('contours', img_contour)
cv2.waitKey(0)
cv2.destroyAllWindows()