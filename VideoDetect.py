import numpy as np
import cv2
import requests
from Stream import Stream
from yolov4 import Detections
import time

vs = Stream('Images/Sample.mp4')
det = Detections()
time.sleep(1.0)

while(vs.isRunning()):

    frame = vs.read()

    img = cv2.imwrite('frame.jpg', frame)
    new_image = cv2.imread("frame.jpg")
    frame_detected = det.yolo(new_image)
    
    cv2.imshow('frame',frame_detected)
    if cv2.waitKey(1) & 0xFF == ord('q'):
  	  break

cv2.destroyAllWindows()
vs.stop()