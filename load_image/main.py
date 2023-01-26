import argparse
import cv2
import sys

ap = argparse.ArgumentParser()
ap.add_argument("-i", '--image', required=True, help='Path to input image')
ap.add_argument("-o", '--output', required=True, help='Path to save the image')
ap.add_argument("-m", '--mode', required=False, help='The image read mode')
args = vars(ap.parse_args())

image_ext = args['image'].split('.')[1]

print(cv2.IMREAD_GRAYSCALE)
if args['mode'] in ['1', '4']:
  image = cv2.imread(args['image'], cv2.IMREAD_COLOR)
  print(image.shape)
  (h, w, c) = image.shape[:3]
  print("width: {} pixels".format(w))
  print("height: {} pixels".format(h))
  print("channels: {} pixels".format(c))
elif args['mode'] == '2':
  image = cv2.imread(args['image'], cv2.IMREAD_GRAYSCALE)
  print(image.shape)
  (h, w) = image.shape[:2]
  print("width: {} pixels".format(w))
  print("height: {} pixels".format(h))
else:
  print("Not implemented")

cv2.imshow("Image", image)
cv2.waitKey(0)

cv2.imwrite("{}.{}".format(args['output'], image_ext), image)
