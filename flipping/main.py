import numpy as np
import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", '--image', type=str, default='nature.jpeg', help='Path to input image')
args = vars(ap.parse_args())

# load the original input image and display it to oour screen
image = cv2.imread(args['image'])
cv2.imshow("Original", image)

# flip the image horizontally
print("[INFO] flipping image horizontally...")
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

# flip the image vertically
flipped = cv2.flip(image, 0)
print("[INFO] flipping image vertically...")
cv2.imshow("Flipped vertically", flipped)

# flip the image along both axes
flipped = cv2.flip(image, -1)
print("[INFO] flipping image horizontally and vertically...")
cv2.imshow("Flipped horizontally and vertically", flipped)
cv2.waitKey(0)
