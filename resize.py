import numpy as np
import argparse
import cv2

# wrap function
def resize(image,width = None,height = None,inter = cv2.INTER_AREA):
	dim = None
	if width is None and height is None:
		return image

	(h,w) = image.shape[:2]

	if height is None:# resize by width
		r = width / float(w)
		dim = (width,int(h*r))
	else: # resize by height
		r = height / float(h)
		dim = (int(w*r),height)

	resized = cv2.resize(image,dim,interpolation = inter)
	return resized


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0]*r))

resized = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (width)", resized)

r = 50.0 / image.shape[0]
dim = (int(image.shape[1]*r),50)

resized = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (height)", resized)

resized = resize(image,height = 50)
cv2.imshow("Resized by function", resized)
cv2.waitKey(0)