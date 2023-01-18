import numpy as np
import cv2

color = cv2.imread('../images/cocacola.jpeg', 1) # 1 - full color load
gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
cv2.imwrite("cocacola-gray.jpeg", gray)

b = color[:, :, 0]
g = color[:, :, 1]
r = color[:, :, 2]

rgba = cv2.merge((b,g,r,g))
cv2.imwrite("cocacola-rgba.png", rgba)
