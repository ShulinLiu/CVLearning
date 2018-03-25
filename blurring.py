import argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# cv2.blur(image, sizeofkernel)
# blur image with increasing-sized kernel, the more blur the image is
blurred = np.hstack([
	cv2.blur(image,(3,3)),
	cv2.blur(image,(5,5)),
	cv2.blur(image,(7,7))])
cv2.imshow("Averaged",blurred)
cv2.waitKey(0)

# Guassian blurring
# cv2.GaussianBlur(image, sizeofkernel,sigma) 
# standard deviation in the x-axis direction
blurred = np.hstack([
	cv2.GaussianBlur(image,(3,3),0),
	cv2.GaussianBlur(image,(5,5),0),
	cv2.GaussianBlur(image,(7,7),0)])
cv2.imshow("Gaussian",blurred)
cv2.waitKey(0)

# Median blurring
# cv2.medianBlur(image, sizeofkernel) 
blurred = np.hstack([
	cv2.medianBlur(image,3),
	cv2.medianBlur(image,5),
	cv2.medianBlur(image,7)])
cv2.imshow("Median",blurred)
cv2.waitKey(0)

# bilateral filter
# preserve edages of an image, reduce noise
# cv2.bilateralFliter(image, neighborhoodsize,colorsigma,spacesigma) 
# neighborhoodsize: diameter of pixel neighborhood
# color sigma:more color in the neighborhood will be cinsidered when computing blur
# space sigma:pixel farther out from the central pixel will infuence blurring calculation
blurred = np.hstack([
	cv2.bilateralFilter(image,5,21,21),
	cv2.bilateralFilter(image,7,31,31),
	cv2.bilateralFilter(image,9,41,41)])
cv2.imshow("Bilateral",blurred)
cv2.waitKey(0)
