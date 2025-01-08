import cv2 as cv

capture = cv.VideoCapture('data/videos/dog.mp4') ## videos is download from https://github.com/jasmcaus/opencv-course/tree/master/Resources/Videos

while True:
    isTrue, frame = capture.read() # Read the video frame by frame
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'): # Press 'd' to break the loop. why 20? 20ms delay between each frame
        break

capture.release() # Release the video capture object from the memory
cv.destroyAllWindows()