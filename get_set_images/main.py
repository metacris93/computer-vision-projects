import argparse
import cv2
import sys

ap = argparse.ArgumentParser()
ap.add_argument("-i", '--image', required=True, help='Path to input image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'], cv2.IMREAD_COLOR)
(h, w) = image.shape[:2]
print("height: {} pixels - width: {} pixels".format(h, w))
cv2.imshow("Original", image)

(b,g,r) = image[0, 0]
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

(b,g,r) = image[200, 300]
print("Pixel at (300, 200) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

image[200,300] = (0,0,255)

# compute the center of the image
(cX, cY) = (w // 2, h // 2)
tl = image[0:cY, 0:cX]
cv2.imshow("Top Left Corner", tl)

tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("Top-Right corner", tr)
cv2.imshow("Bottom-Right corner", br)
cv2.imshow("Bottom-Left corner", bl)

image[0:cY, 0:cX] = (0, 255, 0)
cv2.imshow("Updated", image)

cv2.waitKey(0)
