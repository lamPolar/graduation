import cv2
import numpy as np

#bgr to hsv
color = [49,38,136]
pixel = np.uint8([[color]])
hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)
hsv = hsv[0][0]

print("bgr : ", color)
print("hsv : ", hsv)