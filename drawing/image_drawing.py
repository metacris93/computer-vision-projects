import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", '--image', required=True, help='Path to input image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
(h, w) = image.shape[:2]
print("height: {} pixels - width: {} pixels".format(h, w))

cv2.circle(image, (270, 150), 25, (0,0,255), -1)
cv2.circle(image, (360, 120), 25, (0,0,255), -1)
cv2.rectangle(image, (300,210), (400,240), (0,0,255), -1)

cv2.imshow("Canvas", image)
cv2.waitKey(0)
