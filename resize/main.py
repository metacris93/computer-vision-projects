import numpy as np
import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", '--image', type=str, default='nature.jpeg', help='Path to input image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("Original", image)

# lets resize our image to be 150 pixels wide, but in order to
# prevent our resized image from being skewed/distorted, we must
# first calculate the radio of the *new* width to the *old* width
r = 150 / image.shape[1]
dim = (150, int(image.shape[0] * r))

# perform the actual resizing of the image
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (width)", resized)

# lets resize the image to have a width of 50 pixels, again keeping
# in mind the aspect ratio
r = 50 / image.shape[0]
dim = (int(image.shape[1] * r), 50)

# perform the resizing
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)

# calculating the ratio each and every time we want to resize an image
# let's use the imutils convenience function which will automatically mantain our aspect ratio
# for us
resized = imutils.resize(image, width=400)
cv2.imshow("Resized ia imutils", resized)

methods = [
  ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
  ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
  ("cv2.INTER_AREA", cv2.INTER_AREA),
  ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
  ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)
]
for (name, method) in methods:
  print("[INFO] {}".format(name))
  resized = imutils.resize(image, width=image.shape[1] * 3, inter=method)
  cv2.imshow("Method: {}".format(name), resized)
  cv2.waitKey(0)
