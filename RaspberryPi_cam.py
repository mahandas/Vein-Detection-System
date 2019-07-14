# import  the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

def nothing(x):
    pass
cap = cv2.VideoCapture(0)
# Create a window
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('CLimit','image',0,8,nothing)
r = 1.4

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Our operations on the frame come here
    #convert and put clahe
    clahe = cv2.createCLAHE(clipLimit=r, tileGridSize=(9,9))
    cl1 = clahe.apply(gray)
   
    # Display the resulting frame
    cv2.imshow("image",cl1)
    k = cv2.waitKey(1) & 0xFF

    #capture the image on screen by pressing 'a' and break
    if k == ord("a"):
            cv2.imwrite(time.strftime("Screenshot%Y%m%d%H%M%S.jpg"),cl1)
            cv2.imwrite("temp.jpg",cl1)
            break
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if k == ord("q"):
            break
    # get current positions of trackbar
    p = cv2.getTrackbarPos('CLimit','image')
    r = 0.5 + (p/2)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
