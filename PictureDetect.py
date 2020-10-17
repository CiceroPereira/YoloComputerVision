import numpy as np
import cv2
from yolov4 import Detections



#string = "Images/knife_" + str(i) + ".JPG"
img = cv2.imread("Images/knife_54.JPG")
det = Detections()
img = det.yolo(img)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
