import numpy as np
import cv2
from Stream import Stream
from yolov4 import Detections
import time

pathOut = 'video.mp4'
vs = Stream('Images/Sample02.mp4')
det = Detections()
fps = 60
frame_array = []
time.sleep(1.0)

while(vs.isRunning()):

    frame = vs.read()
    img = cv2.imwrite('frame.jpg', frame)
    new_image = cv2.imread("frame.jpg")
    height, width, layers = new_image.shape
    frame_array.append(new_image)
    frame_detected = det.yolo(new_image)
    
    cv2.imshow('frame',frame_detected)
    if cv2.waitKey(1) & 0xFF == ord('q'):
  	  break

cv2.destroyAllWindows()
vs.stop()
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(pathOut,fourcc, fps, (640,480))

for i in range(len(frame_array)):
    frame = cv2.resize(frame_array[i], (640, 480))
    out.write(frame)
out.release()