import cv2
import os

video_path = os.path.join('data', 'videos', 'dog.mp4') ## videos is download from https://github.com/jasmcaus/opencv-course/tree/master/Resources/Videos
capture = cv2.VideoCapture(video_path) 

ret = True
while ret:
    ret, frame = capture.read() # Read the video frame by frame
    
    # wait time is calculated based on the frames per second of the video
    # if an video is 50fps, then 1000ms/50fps = 20ms, so we need to wait 20ms to get the next frame
    if ret:
        cv2.imshow('Video', frame)
        cv2.waitKey(20) # wait for 20ms before the next frame is displayed

capture.release() # Release the video capture object from the memory
cv2.destroyAllWindows()