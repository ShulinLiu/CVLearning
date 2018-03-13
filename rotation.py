import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,help = "Path to the image")
args = vars(ap.parse_args())

def rotate(image,angle,center = None,scale=1.0):
	(h,w) = image.shape[:2]
	if center is None:
		center = (w/2,h/2)

	M = cv2.getRotationMatrix2D(center,angle,scale)
	rotated = cv2.warpAffine(image,M,(w,h))
	return rotated


image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(h,w) = image.shape[:2]
center = (w//2,h//2)

# M = cv2.getRotationMatrix2D(center,45,1.0)
# rotated = cv2.warpAffine(image,M,(w,h))
rotated = rotate(image,45,center)
cv2.imshow("Ratated by 45 Degrees",rotated)

# M = cv2.getRotationMatrix2D(center,-90,1.0)
# rotated = cv2.warpAffine(image,M,(w,h))
rotated = rotate(image,-90,center)
cv2.imshow("Ratated by -90 Degrees",rotated)
cv2.waitKey(0)
