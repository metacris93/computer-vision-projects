import numpy as np
import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", '--image', type=str, default='logo.png', help='Path to input image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("Original", image)

# NOTE: translating an image is given by a numpy Matrix in the form:
# [
#   [1, 0, shiftX],
#   [0, 1, shiftY],
# ]
# shit the image 25 pixels to the rightand 50 pixels down
M = np.float32([[1,0,25], [0,1,50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

M = np.float32([[1,0,-50], [0,1,-90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

# use the imutils helper function o translate the image 100 pixels
# down in a single function call
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)

cv2.waitKey(0)
