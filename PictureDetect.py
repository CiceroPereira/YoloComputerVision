import numpy as np
import cv2
from yolov4 import Detections


img = cv2.imread("Images/facaa.JPG")
det = Detections()
img = det.yolo(img)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
