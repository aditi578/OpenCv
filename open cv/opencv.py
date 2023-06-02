import random
import numpy as np
import cv2

img = cv2.imread('../../Downloads/yellow_detect.jpeg', -1)

image = cv2.resize(img, (700, 600))

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([20, 50, 70])
upper = np.array([35, 255, 255])

mask = cv2.inRange(hsv, lower, upper)

cv2.imshow("Image", image)
cv2.imshow("Mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()