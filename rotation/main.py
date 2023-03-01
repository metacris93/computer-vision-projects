import numpy as np
import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", '--image', type=str, default='logo.png', help='Path to input image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("Original", image)

# grab the dimensions of the image and calculate the center of the image
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

# rotate our image by 45 degrees around the center of the image
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 degrees", rotated)

# rotate our image by -90 degrees around the center of the image
M = cv2.getRotationMatrix2D((cX, cY), -90, 0.5)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 degrees", rotated)

# rotate our image around an arbitrary point rather than the center
M = cv2.getRotationMatrix2D((10, 10), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by arbitrary point", rotated)

rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 degrees", rotated)

# rotate our image by 33 degrees counterclockwise, ensuring the
# entire rotated image still views in the viewing area
rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated without cropping", rotated)

for angle in np.arange(0, 360, 15):
	rotated = imutils.rotate_bound(image, angle)
	cv2.imshow("Rotated loop (Correct)", rotated)
	cv2.waitKey(0)
