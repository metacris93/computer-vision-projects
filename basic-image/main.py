import numpy as np
import cv2

img = cv2.imread('../images/opencv-logo.webp')
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)
cv2.waitKey(0)

"""
type(img)
> class 'numpy.ndarray'

len(img)
> 900

len(img[0])
> 680

len(img[0][0])
> 3

img.shape
> (900, 680, 3)

img.dtype
dtype('uint8')
"""